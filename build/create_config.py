"""
Commitify - Fake Commit Generator for GitHub

Copyright (C) 2024-2024 Liam Arguedas

This file is part of Commitify, a free CLI tool designed to generate fake commits
for GitHub repositories.

Commitify is distributed under the terms of the GNU General Public License (GPL),
either version 3 of the License, or any later version.

Commitify is provided "as is", without warranty of any kind, express or implied,
including but not limited to the warranties of merchantability, fitness for a
particular purpose, and noninfringement. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
Commitify. If not, see <https://www.gnu.org/licenses/>.
"""

from pathlib import Path
import json


BLANK = ""


class CommitifyConfig:

    def __init__(self):
        self.cfg_dir = Path(__file__).parents[1] / "src" / "cfg"
        self.repository = None
        self.branch = "master"
        self.commits = ""
        self.file = "py"

    def load_settings(self):
        if self.repository == BLANK:
            print("Repository not detected, please reconfigure: ")
        return {
            "repository": self.repository,
            "branch": "master" if self.branch == BLANK else self.branch,
            "commits": self.commits,
            "file": "py" if self.file == BLANK else self.file,
        }

    def ask_configs(self, return_repo_info=False):
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

        print("SETTINGS: Loaded ----------- ")
        print(f'Repository: {configs["repository"]}')
        print(f'Branch: {configs["branch"]}')
        print(
            f'Commits: {"random" if configs["commits"] == BLANK else configs["commits"]}'
        )
        print(f'File: {configs["file"]}')

        print("-----------------------------")
        if return_repo_info:
            return self.repository

    def save_configs(self, cfgs):
        with open(self.cfg_dir / "config.json", "w", encoding="utf-8") as file:
            json.dump(cfgs, file)
