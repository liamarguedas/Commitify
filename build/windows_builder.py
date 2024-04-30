import os
import subprocess
import shutil
from pathlib import Path

GIT_EXTENSION = ".git"


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
        if os.path.exists(self.startup_dir / "Commitify.bat"):
            os.remove(self.startup_dir / "Commitify.bat")

    def create_startup_script(self):
        """TODO"""
        main = self.root_commitify / "main.py"
        with open(self.startup_dir / "Commitify.bat", "w", encoding="utf-8") as file:
            file.write("@echo off\n")
            file.write(f"python {main}")

    def init_repo(self):
        """TODO"""
        print("init local repository")
        command = "git init"
        with subprocess.Popen(command, cwd=self.root_commitify) as process:
            process.wait()

    def config_repo(self, repo):
        """TODO"""
        self.init_repo()
        if not repo[-4:] == GIT_EXTENSION:
            repo = f"{repo}.git"
        print(f"adding remote origin at {repo}")
        command = f"git remote add origin {repo}"
        with subprocess.Popen(command, cwd=self.root_commitify) as process:
            process.wait()

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
