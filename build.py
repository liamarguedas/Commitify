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

import platform
import os
import sys
from pathlib import Path
from build import WinBuilt
from build import CommitifyConfig

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"
COMMITIFY = Path(__file__).parents[0]


def main():

    print("========= COMMITIFY =========")
    print("SETUP: Installing Requirements...")
    install_requirements()

    config = CommitifyConfig()

    print("SETTINGS: Commitify configuration")
    repo = config.ask_configs(return_repo_info=True)

    if user_system_using(WINDOWS):
        print("BUILDING: Building Commitify for Windows")

        builder = WinBuilt()
        print("BUILDING: Creating Root Files")
        builder.set_root()
        print("BUILDING: Creating Git Configuration Files")
        builder.create_git_bat(repo)
        print("BUILDING: Creating Startup Files")
        builder.create_startup_script()
        print("BUILDING: Moving Commitify to Root")
        builder.move_files()
        print("BUILDING: Initializing Git")
        builder.config_repo()

    if user_system_using(LINUX):
        sys.exit(1)  # Kill terminal while in-dev

    if user_system_using(MACOS):
        sys.exit(1)  # Kill terminal while in-dev

    print("DONE: Commitify Completed")
    print("Commitify will automatically run each time your computer starts up.")
    print("For more information visit: https://github.com/liamarguedas/Commitify")


def user_system_using(user_os):
    return platform.system() == user_os


def install_requirements():
    try:
        os.system("pip install -r ./requirements/requirements.txt ")
        print("SETUP: Requirements Installed")
    except Exception as e:
        print(e)
        print("ERROR: Could not install requirements, please install manually")


if __name__ == "__main__":
    main()
