from typing import List
from parser.yacc import yacc_parser, Node

from Commands.cat import Cat
from Commands.echo import Echo
from Commands.pwd import Pwd
from Commands.wc import Wc
from Commands.exit import Exit
from Commands.eq import Eq


class Parser:
    def __init__(self):
        pass

    def __traverse_ast__(self, *, root: Node):
        if root.node_type == Node.NodeType.command:
            # todo dict: str -> constructor ?
            if root.value == '=':
                return [Eq(src=root.children[0], dest=root.children[1])]
            elif root.value == 'cat':
                return [Cat(args=root.children)]
            elif root.value == 'echo':
                return [Echo(args=root.children)]
            elif root.value == 'exit':
                return [Exit(args=root.children)]
            elif root.value == 'pwd':
                return [Pwd(args=root.children)]
            elif root.value == 'wc':
                return [Wc(args=root.children)]
            else:
                # todo exception handling
                raise RuntimeError()
        res = []
        for child in root.children:
            res += self.__traverse_ast__(root=child)
        return res

    def parse(self, *, input_data: str):
        ast = yacc_parser.parse(input_data)
        command_list = self.__traverse_ast__(root=ast)
        return command_list
