#!/usr/bin/env python3

import sys
from datetime import datetime

import dotenv
from github import Github

dotenv.load_dotenv()


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

    def connect_to_repo(self):
        g = Github(self.github_token)
        self.repo = g.get_user().get_repo(self.repo_name)

    def set_sub_dir_content(self):
        while not self.sub_dir_content:
            self.sub_dir_content = input("Subdirectory content: ").lower()

    def commit_to_github(self, task: str, short_description: str, duration: int) -> None:
        commit_message = f"Completed '{task}' in {duration} minutes."
        content = (
            f"Task: {task}\n"
            f"Duration: {duration} minute(s)\n"
            f"Description: {short_description}\n"
            f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        path = (
            f"{datetime.now().strftime('%Y')}/"
            f"{datetime.now().strftime('%b').lower()}/"
            f"{self.sub_dir_content}/"
            f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        )
        self.repo.create_file(path, commit_message, content)
        print("Data committed to GitHub successfully!")


class Registratvm:
    def __init__(self, github_repo_manager: GithubRepoManager):
        self.task: str = ""
        self.short_description = ""
        self.duration: int = 0
        self.github_repo_manager = github_repo_manager

    def start(self):
        github_manager.set_sub_dir_content()
        self.task = input("Enter task name: ").lower().replace(" ", "-")
        self.short_description = input("Enter short description: ").lower()
        self.duration = int(input("Enter duration (minutes): "))

        while True:

            action = input("[*] Persist (y/n): ").lower()
            if action == "y":
                self.github_repo_manager.commit_to_github(
                    task=self.task, duration=self.duration, short_description=self.short_description
                )
                break
            else:
                print("Data not persisted")
                break


if __name__ == "__main__":
    github_manager = GithubRepoManager()
    registratvm = Registratvm(github_manager)
    registratvm.start()
    sys.exit()
