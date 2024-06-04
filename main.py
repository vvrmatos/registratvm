#!/usr/bin/env python3

import time
import sqlite3

from datetime import datetime

import dotenv
from github import Github


dotenv.load_dotenv()

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task TEXT,
                duration INTEGER,
                completed BOOLEAN DEFAULT 0,
                completed_at TIMESTAMP
            )"""
)
conn.commit()

github_token = dotenv.get_key("./.env", "GITHUB_ACCESS_TOKEN")
repo_name = dotenv.get_key("./.env", "GITHUB_REPO_NAME")
g = Github(github_token)
repo = g.get_user().get_repo(repo_name)


class Registratvm:
    def __init__(self):
        pass

    def start(self):
        task = input("Enter task name: ").capitalize()
        duration = int(input("Enter duration (minutes): "))

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration * 60:
                print("Task time elapsed.")
                action = input(
                    "Task not completed yet. Do you want to pause or continue? (pause/continue): "
                ).lower()
                if action == "pause" or action == "p":
                    self.pause_task(task, start_time)
                elif action == "continue" or action == "c":
                    self.continue_task(task, start_time)
                elif action == "quit" or action == "q":
                    break
                else:
                    print("Invalid input. Please enter 'pause' or 'continue', or 'quit'.")
            else:
                time.sleep(10)

        elapsed_time = time.time() - start_time
        self.record_to_database(task, int(elapsed_time / 60), completed=True)

        # Commit data to GitHub
        self.commit_to_github(task, int(elapsed_time / 60))

    def record_to_database(self, task, duration, completed=False):
        c.execute(
            "INSERT INTO tasks (task, duration, completed, completed_at) VALUES (?, ?, ?, ?)",
            (task, duration, completed, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        conn.commit()

    def commit_to_github(self, task, duration):
        commit_message = f"Completed '{task}' in {duration} minutes."
        content = f"Task: {task}\nDuration: {duration} minutes\nCompleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        repo.create_file(
            f"registratvm/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt",
            commit_message,
            content,
        )
        print("Data committed to GitHub successfully!")

    def pause_task(self, task, start_time):
        pause_start_time = time.time()
        input("Task paused. Press Enter to continue...")
        pause_end_time = time.time()
        pause_duration = pause_end_time - pause_start_time
        self.record_to_database(task, int(pause_duration / 60))

    def continue_task(self, task, start_time):
        pass


registratvm = Registratvm()
registratvm.start()
