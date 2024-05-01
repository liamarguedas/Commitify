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

    print("Installing requirements...")
    # install_requirements()

    config = CommitifyConfig()

    print("Commitify configuration")
    repo = config.ask_configs(return_repo_info=True)

    if user_system_using(WINDOWS):

        builder = WinBuilt()
        builder.set_root()
        builder.create_git_bat(repo)
        builder.create_startup_script()
        builder.move_files()
        builder.config_repo()

    if user_system_using(LINUX):

        # TODO
        # LINUX SYSTEM LOGIC HERE
        pass

    if user_system_using(MACOS):

        # TODO
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
