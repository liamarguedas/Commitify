from pathlib import Path
import random
import os
import json


class FileBuilder:

    def __init__(self):
        self.filepath = Path(__file__).parents[0]
        self.txt_path = self.filepath / "txt"
        self.words_file = self.txt_path / "random_words.txt"
        self.file_txt = self.txt_path / "file_txt.txt"
        self.words = self.read_text(self.words_file)
        self.file_text = self.read_text(self.file_txt)
        self.filename = None
        self.filetype = self.read_filetype()

    @staticmethod
    def path_exists(dirname):
        """TODO"""
        return os.path.exists(dirname)

    @staticmethod
    def generate_extra_file(file, dirname):
        """TODO"""
        _splited_file = file.split(".")
        same_name_files = [
            directory_file
            for directory_file in os.listdir(dirname)
            if _splited_file[0] in directory_file
        ]
        return f"{_splited_file[0]}{len(same_name_files) + 1}.{_splited_file[1]}"

    @staticmethod
    def write_new_file(filename):
        """TODO"""
        with open(filename, "w", encoding="utf-8") as file:
            for line in file:
                file.write(line)

    def read_filetype(self):
        """TODO"""
        with open(self.filepath / "cfg" / "config.json", "r", encoding="utf-8") as file:
            return json.load(file)["file"]

    def file_in_path(self, dirname):
        """TODO"""
        return os.path.exists(f"{dirname}/{self.filename}")

    def generate_name(self):
        """TODO"""
        self.filename = f"{random.choice(self.words)}.{self.filetype}"
        return self.filename

    def read_text(self, file):
        """TODO"""
        if self.path_exists(file):
            with open(file, "r", encoding="utf-8") as loaded_file:
                return [line.rstrip("\n") for line in loaded_file.readlines()]
        return ["file"]

    def create_file(self, dirname):
        """TODO"""
        if self.path_exists(dirname):
            file = self.generate_name()
            if self.file_in_path(dirname):
                file = self.generate_extra_file(file, dirname)
            self.write_new_file(file)
