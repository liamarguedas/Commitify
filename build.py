import platform
from pathlib import Path
from build import WinBuilt

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"
COMMITIFY = Path(__file__).parents[0]


def main():
    """TODO"""

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


def user_system_using(os):
    """TODO"""
    return platform.system() == os


if __name__ == "__main__":
    main()
