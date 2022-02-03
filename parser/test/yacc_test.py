from parser.impl import Parser

from Commands.cat import Cat
from Commands.echo import Echo
from Commands.pwd import Pwd
from Commands.wc import Wc
from Commands.exit import Exit
from Commands.eq import Eq


def test_basic():
    parser = Parser()
    res = parser.parse(input_data="cat \"Hello World\" '$varName'")
    assert res == [
        Cat(args=['Hello World', '$varName'])
    ]

