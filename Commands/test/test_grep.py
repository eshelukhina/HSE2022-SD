import argparse
from argparse import Namespace

import pytest

from Commands.grep import Grep, ArgumentParserError


def test_parse_arguments_without_files():
    args = ["str"]
    grep = Grep(args=args)
    with pytest.raises(ArgumentParserError):
        grep.parse_arguments(args)


def test_parse_arguments_with_one_file_and_no_flags():
    args = ["str", "file.txt"]
    result = Namespace(pattern="str", files=["file.txt"], count=None, case_insensitive=False, words=False)
    grep = Grep(args=args)
    output = grep.parse_arguments(args)
    assert output == result


def test_parse_arguments_with_files_and_no_flags():
    args = ["str", "file.txt", "file2.txt", "file3.txt"]
    result = Namespace(pattern="str", files=["file.txt", "file2.txt", "file3.txt"], count=None, case_insensitive=False,
                       words=False)
    grep = Grep(args=args)
    output = grep.parse_arguments(args)
    assert output == result


def test_parse_arguments_with_one_file_and_words_flag():
    args = ["-w", "str", "file.txt"]
    result = Namespace(pattern="str", files=["file.txt"], count=None, case_insensitive=False, words=True)
    grep = Grep(args=args)
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "-w", "file.txt"]
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "file.txt", "-w"]
    output = grep.parse_arguments(args)
    assert output == result


def test_parse_arguments_with_one_file_and_case_insensitive_flag():
    args = ["-i", "str", "file.txt"]
    result = Namespace(pattern="str", files=["file.txt"], count=None, case_insensitive=True, words=False)
    grep = Grep(args=args)
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "-i", "file.txt"]
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "file.txt", "-i"]
    output = grep.parse_arguments(args)
    assert output == result


def test_parse_arguments_with_one_file_and_count_flag():
    args = ["-A", "str", "file.txt"]
    grep = Grep(args=args)
    with pytest.raises(argparse.ArgumentError):
        grep.parse_arguments(args)
    args = ["-A", "0", "str", "file.txt"]
    result = Namespace(pattern="str", files=["file.txt"], count=0, case_insensitive=False, words=False)
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "file.txt", "-A", "0"]
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "-A", "0", "file.txt"]
    output = grep.parse_arguments(args)
    assert output == result
    args = ["str", "file.txt", "-A", "0"]
    output = grep.parse_arguments(args)
    assert output == result


def test_parse_arguments_with_all_flags():
    args = ["-A", "0", "-w", "-i", "str", "file.txt"]
    grep = Grep(args=args)
    result = Namespace(pattern="str", files=["file.txt"], count=0, case_insensitive=True, words=True)
    output = grep.parse_arguments(args)
    assert output == result
