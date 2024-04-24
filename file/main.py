from pathlib import Path

from src import FileBuilder
from src import GitBuilder


def main():
    """TODO"""
    PATH = Path(__file__) / "file"

    # build file
    file = FileBuilder()
    file.create_file(dirname=PATH)

    # add, commit then push file to repo
    git = GitBuilder()
    git.execute()


if __name__ == "__main__":
    main()
