# Authors: Liam Arguedas <iliamftw2013@gmail.com>
# License: BSD 3 clause

from comment_builder import CommentBuilder
import os


class GitBuilder(CommentBuilder):

    def __init__(self, commits=10):
        self.number_of_commits = commits

    def add(self, query="git add", files="."):
        query_to_send = query + " " + files
        os.system(query_to_send)

    def commit(self, query="git commit")
