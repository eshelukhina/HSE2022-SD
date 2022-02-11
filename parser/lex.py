import ply.lex as lex


tokens = (
    'PIPE',
    'EQ',
    'SYMBOLS',
    'DOUBLE_QUOTES',
    'SINGLE_QUOTES',
)

t_PIPE = r'\|'
t_EQ = r'='


def t_SINGLE_QUOTES(t):
    r"\'[^']+\'"
    return t


def t_DOUBLE_QUOTES(t):
    r'"[^\"]+"'
    return t


def t_SYMBOLS(t):
    r'[^\s|=\'\"]+'
    return t


t_ignore = ' \t'


def t_error(t):
    raise ValueError(
        f'Could not tokenize input. Starting from line number: {t.lexer.lineno}'
    )


lexer = lex.lex()
