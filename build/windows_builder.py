import os
import shutil
from pathlib import Path


class WinBuilt:
    """TODO"""

    def __init__(self):
        """TODO"""
        self.root_dir = Path.home()
        self.commitify_folder = Path(__file__).parents[1]
        self.commitify_foldername = "Commitify"
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

    def commitify_exists(self):
        """TODO"""
        return os.path.exists(self.root_dir / self.commitify_foldername)

    def set_root(self):
        """TODO"""
        if not self.commitify_exists():
            os.makedirs(self.commitify_foldername)

    def set_startup(self, file):
        shutil.move(self.commitify_foler / file, self.startup_dir)
