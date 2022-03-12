from typing import List
from parser.parser import Parser, TokenType, Token

p = Parser()


def test_simple():
    input = 'echo \"file.txt\" | cat'
    result = p.tokenize(input)
    print(result)
    assert result == [
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='file.txt', type=TokenType.ARG),
        Token(value='|', type=TokenType.PIPE),
        Token(value='cat', type=TokenType.COMMAND),
    ]


def test_quotes_merge():
    input = 'echo "README".md'
    result = p.tokenize(input)
    assert result == [
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='README.md', type=TokenType.ARG),
    ]


def test_quotes_merge_with_spaces():
    input = "echo 'Hello my name is 'Daniel.' Bye World!'"
    result = p.tokenize(input)
    assert result == [
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='Hello my name is Daniel. Bye World!', type=TokenType.ARG),
    ]


def test_nested_quotes():
    input = "echo 'Hello world...\"meow\"...'"
    result = p.tokenize(input)
    assert result == [
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='Hello world...\"meow\"...', type=TokenType.ARG),
    ]


def test_pipe():
    input = "echo file.txt|cat"
    expected = [
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='file.txt', type=TokenType.ARG),
        Token(value='|', type=TokenType.PIPE),
        Token(value='cat', type=TokenType.COMMAND),
    ]
    result = p.tokenize(input)
    assert result == expected

    input = "echo file.txt| cat"
    result = p.tokenize(input)
    assert result == expected

    input = "echo file.txt |cat"
    result = p.tokenize(input)
    assert result == expected


def test_eq():
    input = "x='Hello World!'"
    result = p.tokenize(input)
    for elem in result:
        print(elem)
    assert result == [
        Token(value='x', type=TokenType.ARG),
        Token(value='=', type=TokenType.EQ),
        Token(value='Hello World!', type=TokenType.ARG),
    ]


def test_eq_with_pipe():
    input = "x='Hello World!' | echo 100"
    result = p.tokenize(input)
    assert result == [
        Token(value='x', type=TokenType.ARG),
        Token(value='=', type=TokenType.EQ),
        Token(value='Hello World!', type=TokenType.ARG),
        Token(value='|', type=TokenType.PIPE),
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='100', type=TokenType.ARG),
    ]


def test_pipe_in_quotes():
    input = "x='Hello World! | echo'"
    result = p.tokenize(input)
    assert result == [
        Token(value='x', type=TokenType.ARG),
        Token(value='=', type=TokenType.EQ),
        Token(value='Hello World! | echo', type=TokenType.ARG),
    ]


def test_equal_in_quotes():
    input = "echo 'x=5'"
    result = p.tokenize(input)
    assert result == [
        Token(value='echo', type=TokenType.COMMAND),
        Token(value='x=5', type=TokenType.ARG),
    ]


def test_process():
    input = "git checkout -b"
    result = p.tokenize(input)
    assert result == [
        Token(value='git', type=TokenType.ARG),
        Token(value='checkout', type=TokenType.ARG),
        Token(value='-b', type=TokenType.ARG),
    ]


def test_empty_arg():
    input = "echo '' \"\""
    result = p.tokenize(input)
    assert result == [
        Token(value='echo', type=TokenType.COMMAND),
    ]
