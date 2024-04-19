from pathlib import Path
import os


class FileBuilder:
    def __init__(self, filetype="py"):
        self.filetype = filetype
        self.filepath = Path(__file__)
        self.txt_path = self.filepath / "txt"
        self.txt_file = self.txt_path / "random_words.txt"

    def txt_file_exists(self):
        return os.path.exists(self.txt_file)

    def read_text(self):
        if self.txt_file_exists():
            with open(self.txt_file, "r", encoding="utf-8") as file:
                text_file = file.readlines()
            return [line.rstrip("\n") for line in text_file]
        return ["file"]


    def create_file(self)
