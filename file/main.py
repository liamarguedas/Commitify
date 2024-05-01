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

from pathlib import Path
from src import GitBuilder


def main():

    print("========= COMMITIFY =========")
    PATH = Path(__file__).parents[0] / "file"
    git = GitBuilder(diretory=PATH)

    commits = git.get_commits_number()

    for current_commit in range(commits):
        print(f"FLOW: Executing {current_commit}/{commits} commits")
        git.execute()
        print("FLOW: Completed")


if __name__ == "__main__":
    main()
