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

import os
import shutil
from pathlib import Path
from subprocess import Popen

GIT_EXTENSION = ".git"
GIT_BAT = "git_setup.bat"
COMMITIFY_BAT = "Commitify.bat"


class WinBuilt:

    def __init__(self):
        self.root_dir = Path.home()
        self.commitify_folder = Path(__file__).parents[1]
        self.foldername = "Commitify"
        self.root_commitify = self.root_dir / self.foldername
        self.startup_dir = (
            self.root_dir
            / "AppData"
            / "Roaming"
            / "Microsoft"
            / "Windows"
            / "Start Menu"
            / "Programs"
            / "Startup"
        )

    def create_startup_script(self):
        with open(self.startup_dir / COMMITIFY_BAT, "w", encoding="utf-8") as file:
            file.write("@echo off\n")
            file.write(f"cd {self.root_commitify}\n")
            file.write("python main.py")

    def create_git_bat(self, repo):
        if not repo[-4:] == GIT_EXTENSION:
            repo = f"{repo}.git"
        command = f"git remote add origin {repo}"
        with open(self.commitify_folder / GIT_BAT, "w", encoding="utf-8") as file:
            file.write("@echo off\n")
            file.write(f"cd {self.root_commitify}\n")
            file.write("git init\n")
            file.write(command)

    def config_repo(self):
        with Popen(self.commitify_folder / GIT_BAT) as process:
            process.communicate()
        self.delete_git_bat()

    def delete_git_bat(self):
        os.remove(self.commitify_folder / GIT_BAT)

    def commitify_exists(self):
        return os.path.exists(self.root_commitify)

    def exists_in_commitify(self, path):
        return os.path.exists(self.root_commitify / path)

    def commitify_dir(self, path):
        os.makedirs(self.root_commitify / path)

    def set_root(self):
        if not self.commitify_exists():
            os.makedirs(self.root_commitify)

    def move_main(self):
        shutil.move(self.root_commitify / "file" / "main.py", self.root_commitify)

    def move_files(self):
        if not self.exists_in_commitify("src"):
            shutil.move(self.commitify_folder / "src", self.root_commitify)
        if not self.exists_in_commitify("file"):
            shutil.move(self.commitify_folder / "file", self.root_commitify)

        self.move_main()
