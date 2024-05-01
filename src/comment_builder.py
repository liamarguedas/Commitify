# Authors: Liam Arguedas <iliamftw2013@gmail.com>
# License: BSD 3 clause

import json
import os
import random
from pathlib import Path


class CommentBuilder:
    """TODO"""

    def __init__(self):

        # loading paths
        self.filepath = Path(__file__).parents[0]
        self.cfg_path = self.filepath / "cfg"
        self.comments_file = self.cfg_path / "comments.json"

        self.comments = self.load_comments()

    def comments_file_exists(self):
        """TODO"""
        return os.path.exists(self.comments_file)

    def load_comments(self):
        """TODO"""
        if self.comments_file_exists():
            with open(self.comments_file, "r", encoding="utf-8") as file:
                return json.load(file)["comments"]
        return self.generic_comment()

    def generic_comment(self):
        """TODO"""
        return ["Fix( comments.json is not working, fix it )"]

    def comment(self):
        """TODO"""
        return random.choice(self.comments)
