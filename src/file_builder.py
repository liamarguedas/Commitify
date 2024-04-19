from pathlib import Path
import random
import os


class FileBuilder:
    def __init__(self, filetype="py"):
        self.filetype = filetype
        self.filepath = Path(__file__)
        self.txt_path = self.filepath / "txt"
        self.txt_file = self.txt_path / "random_words.txt"
        self.words = self.read_text()

    @staticmethod
    def path_exists(dirname):
        return os.path.exists(dirname)

    @staticmethod
    def generate_extra_file(file, dirname):
        _splited_file = file.split(".")
        same_name_files = [
            directory_file
            for directory_file in os.listdir(dirname)
            if _splited_file[0] in directory_file
        ]
        return f"{_splited_file[0]}{len(same_name_files) + 1}.{_splited_file[1]}"

    def file_in_path(self, dirname):
        return os.path.exists(f"{dirname}/{self.filename}")

    def generate_name(self):
        self.filename = f"{random.choice(self.words)}.{self.filetype}"
        return self.filename

    def txt_file_exists(self):
        return os.path.exists(self.txt_file)

    def read_text(self):

        if self.txt_file_exists():

            with open(self.txt_file, "r", encoding="utf-8") as file:

                text_file = file.readlines()
                return [line.rstrip("\n") for line in text_file]
        return ["file"]

    def create_file(self, dirname: str):

        if self.path_exists(dirname):

            file = self.generate_name()

            if self.file_in_path(dirname):
                file = self.generate_extra_file(file)
