import enum
import ply.yacc as yacc
from parser.lex import tokens


class Node:
    class NodeType(enum.Enum):
        none = 'none'
        args = 'args'
        command = 'command'
        pipe = 'pipe'

    def __init__(self, *, node_type: NodeType, value, children):
        self.node_type = node_type
        self.value = value
        self.children = children

    def __str__(self):
        res = self.node_type.name + ' : ' + self.value.__str__()
        for i, child in enumerate(self.children):

            res += '\n' + str(i) + '-' * 15 + '\n'
            res += child.__str__()
        return res


def p_expr_commands(p):
    '''expr : SYMBOLS
            | SYMBOLS args
            | SYMBOLS EQ SYMBOLS
            | expr PIPE expr'''
    # todo error handling
    if len(p) == 2:
        p[0] = Node(node_type=Node.NodeType.command, value=p[1], children=[])
    elif len(p) == 3:
        p[0] = Node(node_type=Node.NodeType.command, value=p[1], children=p[2])
    elif len(p) == 4 and p[2] == '=':
        p[0] = Node(node_type=Node.NodeType.command, value=p[2], children=[p[1], p[3]])
    elif len(p) == 4 and p[2] == '|':
        p[0] = Node(node_type=Node.NodeType.none, value=None, children=[p[1], p[3]])
    else:
        raise RuntimeError("Could not parse input. Something bad happened.")


def p_expr_eq_quotes(p):
    '''expr : SYMBOLS EQ SINGLE_QUOTES
            | SYMBOLS EQ DOUBLE_QUOTES'''
    p[0] = Node(node_type=Node.NodeType.command, value=p[2], children=[p[1], p[3][1:-1]])


def p_args(p):
    ''' args : arg
             | args arg'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        print('ERROR')


def p_arg(p):
    'arg : SYMBOLS'
    p[0] = p[1]


def p_arg_quotes(p):
    '''arg  : SINGLE_QUOTES
            | DOUBLE_QUOTES'''
    p[0] = p[1][1:-1]


def p_error(p):
    raise ValueError(f'Could not parse input\n')


precedence = (
    ('left', 'PIPE'),
)


yacc_parser = yacc.yacc()
