import platform

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"


def main():
    """TODO"""
    if user_system_using(WINDOWS):

        # WIN32 SYSTEM LOGIC HERE
        pass

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
