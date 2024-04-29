from pathlib import Path
from src import GitBuilder


def main():
    """TODO"""
    PATH = Path(__file__).parents[0] / "file"
    git = GitBuilder(diretory=PATH)

    n = git.get_commits_number()

    for _ in range(n):
        print(f"Executing {_}/{n} commits")
        git.execute()


if __name__ == "__main__":
    main()
