# Authors: Liam Arguedas <iliamftw2013@gmail.com>
# License: BSD 3 clause

from pathlib import Path
import os
import random
import json
from .comment_builder import CommentBuilder

BLANK = ""


class GitBuilder(CommentBuilder):
    """TODO"""

    def __init__(self, files="."):
        """TODO"""
        super().__init__()
        self.filepath = Path(__file__)
        self.cfgs = self.read_configs()
        self.branch = self.cfgs.branch
        self.files = files
        self.number_of_commits = self.load_commits()

    @staticmethod
    def random_commits(n=25):
        """TODO"""
        return random.randint(1, n)

    def read_configs(self):
        """TODO"""
        with open(self.filepath / "cfg" / "config.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def load_commits(self):
        """TODO"""
        if not self.cfgs.commits == BLANK:
            try:
                return int(self.cfgs.commits)

            except Exception as e:
                print(e)
                print("Could not read commits, using random commits")

        return self.random_commits()

    def add(self):
        """TODO"""
        query_to_send = f"git add {self.files}"
        os.system(query_to_send)

    def commit_message(self):
        """TODO"""
        return self.comment()

    def commit(self, message: str):
        """TODO"""
        query_to_send = f"git commit -m {message}"
        os.system(query_to_send)

    def push(self):
        """TODO"""
        query_to_send = f"git push origin {self.branch}"
        os.system(query_to_send)

    def execute(self):
        """TODO"""
        for _ in range(self.number_of_commits):
            _comment = self.commit_message()
            self.add()
            self.commit(message=_comment)
            self.push()
