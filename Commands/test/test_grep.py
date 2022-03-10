import os
import tempfile
from argparse import Namespace
from typing import List

import pytest

from Commands.grep import Grep, ArgumentParserError
from Executor.context import Context


def create_tmp_file(content):
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(content)
    return fd, path


def body_of_parse_test(args: List[str], result_flags, result_files):
    output, files = Grep.parse_arguments(args)
    assert output == result_flags
    assert files == result_files


def parse_with_exception(args: List[str], exception_message: str):
    with pytest.raises(ArgumentParserError) as e:
        body_of_parse_test(args, None, None)
        assert e.__str__() == exception_message


def test_parse_without_pattern():
    args = []
    exception_message = "the following arguments are required: pattern"
    parse_with_exception(args, exception_message)
    args = ["-A"]
    parse_with_exception(args, exception_message)
    args = ["-A", "1"]
    parse_with_exception(args, exception_message)
    args = ["-w"]
    parse_with_exception(args, exception_message)
    args = ["-i"]
    parse_with_exception(args, exception_message)
    args = ["-w", "-i"]
    parse_with_exception(args, exception_message)
    args = ["-lol"]
    parse_with_exception(args, exception_message)


def test_parse_arguments_without_files():
    args = ["str"]
    result = Namespace(pattern="str", count=0, case_insensitive=False, words=False)
    files = []
    body_of_parse_test(args, result, files)


def test_parse_arguments_with_one_file_and_no_flags():
    args = ["str", "file.txt"]
    result = Namespace(pattern="str", count=0, case_insensitive=False, words=False)
    files = ["file.txt"]
    body_of_parse_test(args, result, files)


def test_parse_arguments_with_files_and_no_flags():
    args = ["str", "file.txt", "file2.txt", "file3.txt"]
    result = Namespace(pattern="str", count=0, case_insensitive=False, words=False)
    files = ["file.txt", "file2.txt", "file3.txt"]
    body_of_parse_test(args, result, files)


def test_parse_arguments_with_one_file_and_words_flag():
    args = ["-w", "str", "file.txt"]
    result = Namespace(pattern="str", count=0, case_insensitive=False, words=True)
    files = ["file.txt"]
    body_of_parse_test(args, result, files)
    args = ["str", "-w", "file.txt"]
    body_of_parse_test(args, result, files)
    args = ["str", "file.txt", "-w"]
    body_of_parse_test(args, result, files)


def test_parse_arguments_with_one_file_and_case_insensitive_flag():
    args = ["-i", "str", "file.txt"]
    result = Namespace(pattern="str", count=0, case_insensitive=True, words=False)
    files = ["file.txt"]
    body_of_parse_test(args, result, files)
    args = ["str", "-i", "file.txt"]
    body_of_parse_test(args, result, files)
    args = ["str", "file.txt", "-i"]
    body_of_parse_test(args, result, files)


def test_parse_arguments_with_one_file_and_count_flag():
    args = ["-A", "str", "file.txt"]
    parse_with_exception(args, "argument -A: invalid int value: 'str'")
    args = ["-A", "0", "str", "file.txt"]
    result = Namespace(pattern="str", count=0, case_insensitive=False, words=False)
    files = ["file.txt"]
    body_of_parse_test(args, result, files)
    args = ["str", "file.txt", "-A", "0"]
    body_of_parse_test(args, result, files)
    args = ["str", "-A", "0", "file.txt"]
    body_of_parse_test(args, result, files)
    args = ["str", "file.txt", "-A", "0"]
    body_of_parse_test(args, result, files)


def test_parse_arguments_with_all_flags():
    args = ["-A", "0", "-w", "-i", "str", "file.txt"]
    result = Namespace(pattern="str", count=0, case_insensitive=True, words=True)
    files = ["file.txt"]
    body_of_parse_test(args, result, files)


def test_simple_string_execute():
    content = 'hello\nworld'
    context = Context()
    _, path = create_tmp_file(content)

    args = ["hello", path]
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f'{path}: hello'
    finally:
        os.remove(path)


def test_or_string_execute():
    content = 'hello world\nbye\nhello bye\ngray'
    context = Context()
    _, path = create_tmp_file(content)

    args = ["hello|bye", path]
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f'{path}: hello world\n{path}: bye\n{path}: hello bye'
    finally:
        os.remove(path)


def test_or_inside_string_execute():
    content = 'gray, grey\ngrey 1233\ngray 1244\nhello world\nend grey'
    context = Context()
    _, path = create_tmp_file(content)

    args = ["gr(a|e)y", path]
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f'{path}: gray, grey\n{path}: grey 1233\n{path}: gray 1244\n{path}: end grey'
    finally:
        os.remove(path)


def test_char_array_string_execute():
    content = "babble\nbebble\nbibble\nbobble\nbubble\nhello world\n babble hello\nno such grep"
    context = Context()
    _, path = create_tmp_file(content)

    args = ["b[aeiou]bble", path]
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == (f"{path}: babble\n{path}: bebble\n{path}: bibble\n"
                          f"{path}: bobble\n{path}: bubble\n{path}:  babble hello")
    finally:
        os.remove(path)


def test_simple_string_multiple_files():
    content1 = "hello world1\nhello1\nworld\nbye"
    content2 = "world\nbye\nhello world2\nhello2"
    context = Context()

    _, path1 = create_tmp_file(content1)
    _, path2 = create_tmp_file(content2)

    args = ["hello", path1, path2]
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f"{path1}: hello world1\n{path1}: hello1\n" + f"{path2}: hello world2\n{path2}: hello2"
    finally:
        os.remove(path1)
        os.remove(path2)


def test_ignore_case():
    content = "Hello IM PASHA\nhello IM KATYA"
    context = Context()

    _, path = create_tmp_file(content)

    args = ["Hello", path, '-i']
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f'{path}: Hello IM PASHA\n{path}: hello IM KATYA'
    finally:
        os.remove(path)


def test_ignore_case_two_files():
    content1 = "Hello World\n hello world"
    content2 = "Hello World1\n hello world"

    context = Context()
    _, path1 = create_tmp_file(content1)
    _, path2 = create_tmp_file(content2)

    args = ["hello", "-i", path1, path2]
    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f"{path1}: Hello World\n{path1}:  hello world\n" + f"{path2}: Hello World1\n{path2}:  hello world"
    finally:
        os.remove(path1)
        os.remove(path2)


def test_search_like_word():
    content = "hello worldmy name id daniel\nhello world"
    context = Context()
    _, path = create_tmp_file(content)
    args = ["hello world", "-w", path]

    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f"{path}: hello world"
    finally:
        os.remove(path)


def test_use_flag_a():
    content = "hello\nworld1\nworld2\nworld3\nworld4\nworld5"
    context = Context()
    _, path = create_tmp_file(content)
    args = ["hello", "-A", "5", path]

    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f"{path}: hello\n{path}: world1\n{path}: world2\n{path}: world3\n{path}: world4\n{path}: world5"
    finally:
        os.remove(path)


def test_use_flag_a_double_find():
    content = "hello\nhello\nworld2\nworld3\nworld4\nworld5"
    context = Context()
    _, path = create_tmp_file(content)
    args = ["hello", "-A", "3", path]

    grep = Grep(args=args)
    try:
        output, ret_code = grep.execute(context)

        assert ret_code == 0
        assert output == f"{path}: hello\n{path}: hello\n{path}: world2\n{path}: world3\n{path}: world4"
    finally:
        os.remove(path)
