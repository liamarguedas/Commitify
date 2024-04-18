from pathlib import Path


class FileBuilder:
    def __init__(self, filetype="py"):
        self.filetype = filetype
        self.filepath = Path(__file__)
        self.txt_path = self.filepath / "txt"
        self.txt_file = self.txt_path / "random_words.txt"
