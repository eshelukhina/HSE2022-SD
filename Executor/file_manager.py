import os
from os import path, walk

from Executor.path_types import PathTypes


class FileManager:
    def __init__(self, file_path: str):
        self.file_type = PathTypes.unknown
        self.path_to_file = file_path

    def get_file_type(self):
        if path.isfile(self.path_to_file):
            self.file_type = PathTypes.file
            return self.file_type
        elif path.isdir(self.path_to_file):
            self.file_type = PathTypes.directory
            return self.file_type
        else:
            return self.file_type

    def get_file_content(self):
        if self.file_type == PathTypes.file:
            f = open(self.path_to_file, "r")
            return str(f.read())
        elif self.file_type == PathTypes.directory:
            filenames = next(walk(self.path_to_file), (None, None, []))[2]
            result = "".join(file + '\n' for file in filenames)
            return result
        else:
            raise Exception('Unknown type of file!')

    @staticmethod
    def get_current_directory():
        return os.getcwd()


