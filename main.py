#!/usr/bin/env python3

import sys
import time

import dotenv

# from collections import namedtuple
from datetime import datetime
from github import Github

dotenv.load_dotenv()


# TODO: Add a database for data persistence?


class GithubRepoManager:
    def __init__(self, env_file_path="./.env"):
        self.env_file_path = env_file_path
        self.github_token = None
        self.repo_name = None
        self.repo = None
        self.sub_dir_content = ""
        self.initialize()
        self.connect_to_repo()

    def initialize(self):
        self.github_token = dotenv.get_key(self.env_file_path, "GITHUB_ACCESS_TOKEN")
        self.repo_name = dotenv.get_key(self.env_file_path, "GITHUB_REPO_NAME")
        # TODO: Set encapsulation with regex pattern or options menu ["python", "math", "etc"]
        while not self.sub_dir_content:
            self.sub_dir_content = input("Subdirectory content: ").lower()

    def connect_to_repo(self):
        g = Github(self.github_token)
        self.repo = g.get_user().get_repo(self.repo_name)

    def commit_to_github(self, task: str, duration: int) -> None:
        commit_message = f"Completed '{task}' in {duration} minutes."
        content = f"Task: {task}\nDuration: {duration} minute(s)\nCompleted at: {datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')}"
        self.repo.create_file(
            f"{datetime.now().strftime('%Y')}/{datetime.now().strftime('%b').lower()}/{self.sub_dir_content}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt",
            commit_message,
            content
        )
        print("Data committed to GitHub successfully!")


class Registratvm:
    def __init__(self, github_repo_manager: GithubRepoManager):
        self.task: str = ""
        self.duration: int = 0
        self.github_repo_manager = github_repo_manager

    def start(self):
        self.task = '-'.join(input("Enter task name: ").lower().split())
        self.duration = int(input("Enter duration (minutes): "))

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= self.duration * 60:
                print("Task time elapsed.")
                action = input(
                    "[*] Persist (y/n): "
                ).lower()
                if action == "y":
                    self.github_repo_manager.commit_to_github(task=self.task, duration=self.duration)
                    break
                else:
                    print("Data not persisted")
                    break
            else:
                time.sleep(10)


github_manager = GithubRepoManager()
registratvm = Registratvm(github_manager)
registratvm.start()
sys.exit()
