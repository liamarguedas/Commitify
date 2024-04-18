# Authors: Liam Arguedas <iliamftw2013@gmail.com>
# License: BSD 3 clause

from comment_builder import CommentBuilder
import os


class GitBuilder(CommentBuilder):

    def __init__(self, commits=10, branch="master", files="."):
        super().__init__()
        self.branch = branch
        self.files = files
        self.number_of_commits = commits

    def add(self):
        query_to_send = f"git add {self.files}"
        os.system(query_to_send)

    def commit_message(self):
        return self.comment()

    def commit(self, message: str):
        query_to_send = f"git commit -m {message}"
        os.system(query_to_send)

    def push(self):
        query_to_send = f"git push origin {self.branch}"
        os.system(query_to_send)

    def execute(self):
        for _ in range(self.number_of_commits):
            _comment = self.commit_message()
            self.add()
            self.commit(message=_comment)
            self.push()
