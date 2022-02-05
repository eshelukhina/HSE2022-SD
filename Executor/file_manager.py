import os
from os import path


class FileManager:
    @staticmethod
    def is_file(path_to_file):
        return path.isfile(path_to_file)

    @staticmethod
    def is_directory(path_to_directory):
        return path.isdir(path_to_directory)

    @staticmethod
    def get_file_content(path_to_file):
        with open(path_to_file, "r") as f:
            return str(f.read())

    @staticmethod
    def get_directory_content(path_to_directory):
        return '\n'.join([os.path.join(path_to_directory, x) for x in os.listdir(path_to_directory)])

    @staticmethod
    def get_current_directory():
        return os.getcwd()
