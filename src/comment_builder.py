# Authors: Liam Arguedas <iliamftw2013@gmail.com>
# License: BSD 3 clause

import json
import os
from pathlib import Path


class CommentBuilder:

    def __init__(self):

        # loading paths
        self.filepath = Path(__file__)
        self.cfg_path = self.filepath / "cfg"
        self.comments_file = self.cfg_path / "comments.json"

        self.comments = self.load_comments()

    def comments_file_exists(self):
        return os.path.exists(self.comments_file)

    def load_comments(self):
        if self.comments_file_exists():
            with open(self.comments_file, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except Exception as e:
                    print(e)
                    print(
                        f"Could not read {self.comments_file}, make sure that .json has no errors, default comments have been selected"
                    )
        return self.generic_comment()

    def generic_comment(self):
        return ["Fix( comments.json is not working, fix it )"]
