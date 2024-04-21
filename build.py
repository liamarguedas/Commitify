import platform
import os
from pathlib import Path
from build import WinBuilt

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"
COMMITIFY = Path(__file__).parents[0]


def main():
    """TODO"""

    install_requirements()

    MAIN = COMMITIFY / "file" / "main.py"

    if user_system_using(WINDOWS):

        builder = WinBuilt()
        builder.set_root()

        builder.set_startup(file=MAIN)

    if user_system_using(LINUX):

        # LINUX SYSTEM LOGIC HERE
        pass

    if user_system_using(MACOS):

        # DARWING SYSTEM LOGIC HERE
        pass


def ask_configs():
    repository = input("Repository URL: ")
    branch = lower(input("Branch (master will be used if left blank): "))
    commits = int(input("Daily commits (Maximum 100): "))
    file = lower(input("type of file (py, js, rs, txt):")).replace(".", "")


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
