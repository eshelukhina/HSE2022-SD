import pytest

from Commands.cat import Cat
from Commands.echo import Echo
from Commands.eq import Eq
from Commands.exit import Exit
from Commands.process import Process
from Commands.pwd import Pwd
from Commands.wc import Wc
from parser.parser import Parser
from parser.parser import ParserException

def test_empty():
    parser = Parser()
    res = parser.parse("")
    assert res == []


def test_process():
    parser = Parser()
    res = parser.parse("git checkout -b")
    assert res == [
        Process(name='git', args=['checkout', '-b'])
    ]


def test_basic():
    parser = Parser()
    res = parser.parse("cat \"Hello World\" '$varName'")
    assert res == [
        Cat(args=['Hello World', '$varName'])
    ]


def test_pipe():
    parser = Parser()
    res = parser.parse("echo \"42\" | wc | pwd | exit")
    for elem in res:
        print(elem)
    assert res == [
        Echo(args=['42']),
        Wc(args=[]),
        Pwd(args=[]),
        Exit(args=[])
    ]


def test_eq():
    parser = Parser()
    res = parser.parse("x=\"Golang\" | y = 200 | z= 'damn'")
    assert res == [
        Eq(dest='x', src='Golang'),
        Eq(dest='y', src='200'),
        Eq(dest='z', src='damn')
    ]


def test_command_arguments():
    parser = Parser()
    res = parser.parse("echo echo")
    assert res == [
        Echo(args=["echo"])
    ]


def test_fail_eq():
    parser = Parser()
    res = parser.parse("x=")
    assert res == [
        Eq(dest='x', src=''),
    ]


def test_fail_single_quotes():
    parser = Parser()
    with pytest.raises(ParserException) as e:
        parser.parse("cat \"")
