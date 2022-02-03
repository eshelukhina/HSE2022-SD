import ply.lex as lex


reserved = {
    'cat': 'CAT',
    'echo': 'ECHO',
    'wc': 'WC',
    'pwd': 'PWD',
    'exit': 'EXIT',
}

tokens = (
    'CAT',
    'ECHO',
    'WC',
    'PWD',
    'EXIT',
    'PIPE',
    'EQ',
    'SYMBOLS',
    'DOUBLE_QUOTES',
    'SINGLE_QUOTES',
)

t_CAT = r'cat'
t_ECHO = r'echo'
t_WC = r'wc'
t_PWD = r'pwd'
t_EXIT = r'exit'
t_PIPE = r'\|'
t_EQ = r'='


def t_SINGLE_QUOTES(t):
    r'\'[^\']+\''
    return t


def t_DOUBLE_QUOTES(t):
    r'"[^\"]+"'
    return t


def t_SYMBOLS(t):
    r'[a-zA-Z0-9_$.-]+'
    t.type = reserved.get(t.value, 'SYMBOLS')
    return t


t_ignore = ' \t'


def t_error(t):
    raise RuntimeError(f'Could not tokenize input: {t.value}')


lexer = lex.lex()
