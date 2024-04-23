import os
import subprocess
import shutil
from pathlib import Path


class WinBuilt:
    """TODO"""

    def __init__(self):
        """TODO"""
        self.root_dir = Path.home()
        self.commitify_folder = Path(__file__).parents[1]
        self.foldername = "Commitify"
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

    def init_repo(self):
        """TODO"""
        command = "git init"
        process = subprocess.Popen(command, cwd=self.root_dir / self.foldername)
        process.wait()

    def config_repo(self, repo):
        """TODO"""
        self.init_repo()
        command = f"git remote add origin {repo}"
        process = subprocess.Popen(command, cwd=self.root_dir / self.foldername)
        process.wait()

    def commitify_exists(self):
        """TODO"""
        return os.path.exists(self.root_dir / self.foldername)

    def exists_in_commitify(self, path):
        """TODO"""
        return os.path.exists(self.root_dir / self.foldername / path)

    def commitify_dir(self, path):
        """TODO"""
        os.makedirs(self.root_dir / self.foldername / path)

    def set_root(self):
        """TODO"""
        if not self.commitify_exists():
            os.makedirs(self.root_dir / self.foldername)

    def set_startup(self, file):
        """TODO"""
        shutil.move(self.commitify_folder / file, self.startup_dir)

    def move_files(self):
        """TODO"""
        if not self.exists_in_commitify("src"):
            self.commitify_dir("src")
        if not self.exists_in_commitify("file"):
            self.commitify_dir("file")

        shutil.move(self.commitify_folder / "src", self.root_dir / self.foldername)
