from pathlib import Path

from src import FileBuilder
from src import GitBuilder


def main():
    """TODO"""
    PATH = Path(__file__).parents[0] / "file"
    git = GitBuilder(diretory=PATH)
    git.execute()


if __name__ == "__main__":
    main()
