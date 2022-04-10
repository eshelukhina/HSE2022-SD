from Commands.cat import Cat
from Commands.echo import Echo
from Commands.eq import Eq
from Commands.exit import Exit
from Commands.grep import Grep
from Commands.process import Process
from Commands.pwd import Pwd
from Commands.wc import Wc

from typing import List
from enum import Enum


class ParserException(Exception):
    pass


class TokenType(Enum):
    COMMAND = 0
    ARG = 1
    PIPE = 2
    EQ = 3


class Token:
    value: str
    type: TokenType

    def __init__(self, *, value, type):
        self.value = value
        self.type = type

    def __eq__(self, other):
        return (isinstance(other, Token) and
                self.value == other.value and
                self.type == other.type)

    def __str__(self):
        return f'Token: {self.value}, {self.type}'


class Parser:
    def __init__(self):
        pass

    COMMANDS_LIST = ['cat', 'echo', 'wc', 'pwd', 'grep', 'exit']

    def tokenize(self, input):
        input = input.strip()
        cur = 0
        tokens = []
        cur_token: str = ''
        quotes = None
        while cur < len(input):
            if (input[cur] == '|' or input[cur] == '=') and not quotes:
                if cur_token:
                    tokens.append(cur_token)
                tokens.append(input[cur])
                cur_token = ''
                cur += 1
                continue
            if input[cur] == ' ' and not quotes:
                if cur_token:
                    tokens.append(cur_token)
                    cur_token = ''
                while cur < len(input) and input[cur] == ' ':
                    cur += 1
                continue
            if input[cur] == '\"' or input[cur] == '\'':
                if not quotes:
                    quotes = input[cur]
                    cur += 1
                    continue
                elif quotes == input[cur]:
                    quotes = None
                    cur += 1
                    continue
            cur_token += input[cur]
            cur += 1
        if cur_token:
            tokens.append(cur_token)
        if quotes:
            raise ParserException("Invalid input")
        result = []
        for value in tokens:
            if value in self.COMMANDS_LIST:
                token_type = TokenType.COMMAND
            elif value == '|':
                token_type = TokenType.PIPE
            elif value == '=':
                token_type = TokenType.EQ
            else:
                token_type = TokenType.ARG
            result.append(Token(value=value, type=token_type))
        return result

    def __construct_command__(self, command: List[Token]):
        if len(command) == 0:
            raise ParserException("Empty command in construction")
        if command[0].type == TokenType.COMMAND:
            args = [c.value for c in command[1:]]
            if command[0].value == 'cat':
                return Cat(args=args)
            elif command[0].value == 'echo':
                return Echo(args=args)
            elif command[0].value == 'wc':
                return Wc(args=args)
            elif command[0].value == 'pwd':
                return Pwd(args=args)
            elif command[0].value == 'exit':
                return Exit(args=args)
            elif command[0].value == 'grep':
                return Grep(args=args)
            raise ParserException(f"Command {command[0].value} is not supported")
        if len(command) == 2 and command[0].type == TokenType.ARG and command[1].type == TokenType.EQ:
            return Eq(dest=command[0].value, src="")
        if (len(command) == 3 and command[0].type == TokenType.ARG and
                command[1].type == TokenType.EQ and command[2].type == TokenType.ARG):
            return Eq(dest=command[0].value, src=command[2].value)
        else:
            return Process(name=command[0].value, args=[c.value for c in command[1:]])

    def parse(self, input: str):
        tokens: List[Token] = self.tokenize(input)
        if not tokens:
            return []
        commands: List[List[Token]] = []
        cur_command: List[Token] = []
        if tokens[0].type == TokenType.PIPE:
            raise ParserException('Pipe is not expected at the beginning of command')
        elif tokens[-1].type == TokenType.PIPE:
            raise ParserException('Pipe is not expected at the end of command')
        for i, token in enumerate(tokens):
            if token.type == TokenType.PIPE:
                commands.append(cur_command)
                cur_command = []
            else:
                cur_command.append(token)
        commands.append(cur_command)
        result = []
        for command in commands:
            result.append(self.__construct_command__(command))
        return result
