from pathlib import Path
import json


class CommitifyConfig:
    """TODO"""

    def __init__(self):
        """TODO"""
        self.cfg_dir = Path(__file__).parents[1] / "src" / "cfg"
        self.repository = None
        self.branch = "master"
        self.commits = ""
        self.file = "py"

    def load_settings(self):
        """TODO"""
        return {
            "repository": self.repository,
            "branch": self.branch,
            "commits": self.commits,
            "file": self.file,
        }

    def ask_configs(self, return_repo_info=False):
        """TODO"""
        try:
            self.repository = input("Repository URL: ")
            self.branch = input("Branch (Default: master): ")
            self.commits = input("Number of Daily commits (Default: Random): ")
            self.file = input("Commit File type (Default: py): ")

        except Exception as e:
            print(e)
            print("could not save configs")
            self.repository = input("Repository URL: ")

        configs = self.load_settings()

        self.save_configs(configs)

        print(f"Settings saved: {configs}")

        if return_repo_info:
            return self.repository

    def save_configs(self, cfgs):
        """TODO"""
        with open(self.cfg_dir / "config.json", "w", encoding="utf-8") as file:
            json.dump(cfgs, file)
