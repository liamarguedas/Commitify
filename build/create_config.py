from pathlib import Path
import json


class CommitifyConfig:
    """TODO"""

    def __init__(self):
        """TODO"""
        self.cfg_dir = Path(__file__).parents[1] / "src" / "cfg"
        # defaults
        self.repository = None
        self.branch = "master"
        self.commits = 10
        self.file = "py"
        self.default_settings = {
            "repository": self.repository,
            "branch": self.branch,
            "commits": self.commits,
            "file": self.file,
        }

    def ask_configs(self, return_repo=False):
        """TODO"""
        try:
            self.repository = input("Repository URL: ")
            self.branch = input("Branch (master will be used if blank): ").lower()
            self.commits = int(input("Daily commits (Maximum 100): "))
            self.file = (
                input("type of file (py, js, rs, txt):").replace(".", "").lower()
            )
            self.default_settings = {
                "repository": self.repository,
                "branch": self.branch,
                "commits": self.commits,
                "file": self.file,
            }

        except Exception as e:
            print(e)
            print(f"could not save configs, using defaults: {self.default_settings}")
            self.repository = input("Repository URL: ")
        self.save_configs(self.default_settings)
        if return_repo:
            return self.repository

    def save_configs(self, cfgs):
        """TODO"""
        try:
            with open(self.cfg_dir / "config.json", "w") as file:
                json.dump(cfgs, file)

        except Exception as e:
            print(e)
            print(f"could not save configs, using defaults: {self.default_settings}")
