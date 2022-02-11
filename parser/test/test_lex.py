from typing import List, Tuple, NoReturn

import pytest
from ply.lex import LexToken
from parser.lex import lexer


def tokenize(*, line: str) -> List[LexToken]:
    lexer.input(line)
    return [tok for tok in lexer]


def compare_tokens(*, tokens: List[LexToken], correct_tokens: List[Tuple[str, str]]) -> NoReturn:
    assert len(tokens) == len(correct_tokens)
    for i in range(len(tokens)):
        correct_type, correct_value = correct_tokens[i]
        assert tokens[i].type == correct_type
        assert tokens[i].value == correct_value


def test_command():
    tokens = tokenize(line='wc cat echo pwd exit')
    correct_tokens = [
        ('SYMBOLS', 'wc'),
        ('SYMBOLS', 'cat'),
        ('SYMBOLS', 'echo'),
        ('SYMBOLS', 'pwd'),
        ('SYMBOLS', 'exit'),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_symbol_args():
    tokens = tokenize(line='cat arg1 $varName10 arg3')
    correct_tokens = [
        ('SYMBOLS', 'cat'),
        ('SYMBOLS', 'arg1'),
        ('SYMBOLS', '$varName10'),
        ('SYMBOLS', 'arg3'),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_double_quotes():
    tokens = tokenize(line='echo "$varName" "arg2""arg3" "the cat says \'$x\'" just_symbols')
    correct_tokens = [
        ('SYMBOLS', 'echo'),
        ('DOUBLE_QUOTES', '"$varName"'),
        ('DOUBLE_QUOTES', '"arg2"'),
        ('DOUBLE_QUOTES', '"arg3"'),
        ('DOUBLE_QUOTES', '"the cat says \'$x\'"'),
        ('SYMBOLS', 'just_symbols')
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_single_quotes():
    tokens = tokenize(line="echo '$varName' 'arg1''arg3' just_symbols")
    correct_tokens = [
        ('SYMBOLS', 'echo'),
        ('SINGLE_QUOTES', "'$varName'"),
        ('SINGLE_QUOTES', "'arg1'"),
        ('SINGLE_QUOTES', "'arg3'"),
        ('SYMBOLS', 'just_symbols')
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_pipe():
    tokens = tokenize(line='echo file_name.txt | cat | exit')
    correct_tokens = [
        ('SYMBOLS', 'echo'),
        ('SYMBOLS', 'file_name.txt'),
        ('PIPE', '|'),
        ('SYMBOLS', 'cat'),
        ('PIPE', '|'),
        ('SYMBOLS', 'exit')
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_process():
    tokens = tokenize(line='git checkout -b')
    correct_tokens = [
        ('SYMBOLS', 'git'),
        ('SYMBOLS', 'checkout'),
        ('SYMBOLS', '-b'),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_eq():
    tokens = tokenize(line='x=file_name.txt')
    correct_tokens = [
        ('SYMBOLS', 'x'),
        ('EQ', '='),
        ('SYMBOLS', 'file_name.txt'),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)

    tokens = tokenize(line='x = file_name.txt')
    correct_tokens = [
        ('SYMBOLS', 'x'),
        ('EQ', '='),
        ('SYMBOLS', 'file_name.txt'),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_eq_quotes():
    tokens = tokenize(line="x=\"file_name.txt\"")
    correct_tokens = [
        ('SYMBOLS', 'x'),
        ('EQ', '='),
        ('DOUBLE_QUOTES', "\"file_name.txt\""),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)

    tokens = tokenize(line="x='file_name.txt'")
    correct_tokens = [
        ('SYMBOLS', 'x'),
        ('EQ', '='),
        ('SINGLE_QUOTES', "'file_name.txt'"),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)


def test_empty_arg():
    tokens = tokenize(line="echo '' \"\"")
    correct_tokens = [
        ('SYMBOLS', 'echo'),
        ('SINGLE_QUOTES', '\'\''),
        ('DOUBLE_QUOTES', '\"\"'),
    ]
    compare_tokens(tokens=tokens, correct_tokens=correct_tokens)
