import os
import shutil
from pathlib import Path
from subprocess import Popen

GIT_EXTENSION = ".git"
GIT_BAT = "git_setup.bat"
COMMITIFY_BAT = "Commitify.bat"


class WinBuilt:
    """TODO"""

    def __init__(self):
        """TODO"""
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

    def uninstall_windows_files(self):
        """TODO"""
        if self.commitify_exists():
            shutil.rmtree(self.root_commitify)

        if os.path.exists(self.startup_dir / COMMITIFY_BAT):
            os.remove(self.startup_dir / COMMITIFY_BAT)

    def create_startup_script(self):
        """TODO"""
        main = self.root_commitify / "main.py"
        with open(self.startup_dir / COMMITIFY_BAT, "w", encoding="utf-8") as file:
            file.write("@echo off\n")
            file.write(f"python {main}")

    def create_git_bat(self, repo):
        """TODO"""
        if not repo[-4:] == GIT_EXTENSION:
            repo = f"{repo}.git"
        command = f"git remote add origin {repo}"
        with open(self.commitify_folder / GIT_BAT, "w", encoding="utf-8") as file:
            file.write("@echo off\n")
            file.write(f"cd {self.root_commitify}\n")
            file.write("git init\n")
            file.write(command)

    def config_repo(self):
        """TODO"""
        with Popen(self.commitify_folder / GIT_BAT) as process:
            process.communicate()
        self.delete_git_bat()

    def delete_git_bat(self):
        """TODO"""
        os.remove(self.commitify_folder / GIT_BAT)

    def commitify_exists(self):
        """TODO"""
        return os.path.exists(self.root_commitify)

    def exists_in_commitify(self, path):
        """TODO"""
        return os.path.exists(self.root_commitify / path)

    def commitify_dir(self, path):
        """TODO"""
        os.makedirs(self.root_commitify / path)

    def set_root(self):
        """TODO"""
        if not self.commitify_exists():
            os.makedirs(self.root_commitify)

    def move_main(self):
        """TODO"""
        shutil.move(self.root_commitify / "file" / "main.py", self.root_commitify)

    def move_files(self):
        """TODO"""
        if not self.exists_in_commitify("src"):
            shutil.move(self.commitify_folder / "src", self.root_commitify)
        if not self.exists_in_commitify("file"):
            shutil.move(self.commitify_folder / "file", self.root_commitify)

        self.move_main()
