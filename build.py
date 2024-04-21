import platform
import os
from pathlib import Path
from build import WinBuilt
from build import CommitifyConfig

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"
COMMITIFY = Path(__file__).parents[0]


def main():
    """TODO"""

    install_requirements()

    config = CommitifyConfig()

    repo = config.ask_configs(return_repo=True)

    MAIN = COMMITIFY / "file" / "main.py"

    if user_system_using(WINDOWS):

        builder = WinBuilt()
        builder.set_root()
        builder.init_repo(repo)
        builder.set_startup(file=MAIN)

        builder.set_files()

    if user_system_using(LINUX):

        # LINUX SYSTEM LOGIC HERE
        pass

    if user_system_using(MACOS):

        # DARWING SYSTEM LOGIC HERE
        pass


def user_system_using(user_os):
    """TODO"""
    return platform.system() == user_os


def install_requirements():
    """TODO"""
    try:
        os.system("pip install -r ./requirements/requirements.txt ")
    except Exception as e:
        print(e)
        print("could not install requirements, please install manually")


if __name__ == "__main__":
    main()
