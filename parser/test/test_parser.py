import pytest

from parser.impl import Parser

from Commands.process import Process
from Commands.cat import Cat
from Commands.echo import Echo
from Commands.pwd import Pwd
from Commands.wc import Wc
from Commands.exit import Exit
from Commands.eq import Eq


def test_empty():
    parser = Parser()
    res = parser.parse(input_data="")
    assert res == []


def test_process():
    parser = Parser()
    res = parser.parse(input_data="git checkout -b")
    assert res == [
        Process(name='git', args=['checkout', '-b'])
    ]


def test_basic():
    parser = Parser()
    res = parser.parse(input_data="cat \"Hello World\" '$varName'")
    assert res == [
        Cat(args=['Hello World', '$varName'])
    ]


def test_pipe():
    parser = Parser()
    res = parser.parse(input_data="echo \"42\" | wc | pwd | exit")
    assert res == [
        Echo(args=['42']),
        Wc(args=[]),
        Pwd(args=[]),
        Exit(args=[])
    ]


def test_eq():
    parser = Parser()
    res = parser.parse(input_data="x=\"Golang\" | y = 200 | z= 'damn'")
    assert res == [
        Eq(dest='x', src='Golang'),
        Eq(dest='y', src='200'),
        Eq(dest='z', src='damn')
    ]


def test_command_arguments():
    parser = Parser()
    res = parser.parse(input_data="echo echo")
    assert res == [
        Echo(args=["echo"])
    ]


def test_fail_eq():
    parser = Parser()
    with pytest.raises(ValueError):
        parser.parse(input_data="x=")
