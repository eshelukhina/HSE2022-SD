import os
from os import path


class FileManager:
    """
    The component responsible for working with the file system.
    """

    @staticmethod
    def is_file(path_to_file):
        """
        Check if file exists
        :rtype bool
        """
        return path.isfile(path_to_file)

    @staticmethod
    def get_file_content(path_to_file):
        """
        Returns the file content
        :rtype str
        """
        with open(path_to_file, "r") as f:
            return str(f.read())

    @staticmethod
    def get_directory_content(path_to_directory):
        """
        Returns the names of files in a directory
        :rtype list[str]
        """
        return [os.path.join(path_to_directory, x) for x in os.listdir(path_to_directory)]

    @staticmethod
    def get_current_directory():
        """
        Returns the path to the working directory
        :rtype str
        """
        return os.getcwd()
