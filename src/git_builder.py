# Authors: Liam Arguedas <iliamftw2013@gmail.com>
# License: BSD 3 clause

from pathlib import Path
import random
import os
import json
import time
from .comment_builder import CommentBuilder
from .file_builder import FileBuilder

BLANK = ""


class GitBuilder:
    """TODO"""

    def __init__(self, diretory, files="."):
        """TODO"""
        self.comment_generator = CommentBuilder()
        self.diretory = diretory
        self.file_generator = FileBuilder()
        self.filepath = Path(__file__).parents[0]
        self.cfgs = self.read_configs()
        self.branch = self.cfgs["branch"]
        self.files = files

    @staticmethod
    def random_commits(n=25):
        """TODO"""
        return random.randint(1, n)

    def read_configs(self):
        """TODO"""
        with open(self.filepath / "cfg" / "config.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def get_commits_number(self):
        """TODO"""
        if not self.cfgs["commits"] == BLANK:
            try:
                return int(self.cfgs["commits"])

            except Exception as e:
                print(e)
                print("Could not read commits, using random commits")

        return self.random_commits()

    def add(self):
        """TODO"""
        command = "git add ."
        os.system(command)

    def commit(self, message: str):
        """TODO"""
        command = f'git commit -m "{message}"'
        os.system(command)

    def push(self):
        """TODO"""
        command = f"git push origin {self.branch}"
        os.system(command)

    def execute(self):
        """TODO"""
        self.file_generator.create_file(self.diretory)
        comment = self.comment_generator.comment()
        self.add()
        self.commit(message=comment)
        self.push()
