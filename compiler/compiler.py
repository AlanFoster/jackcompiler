from parser.JackLexer import JackLexer
from parser.JackParser import JackParser


def lex(input_stream: str) -> [str]:
    lexer = JackLexer(input_stream)
    tokens = []

    for token in lexer.getAllTokens():
        tokens.append(
            {
                "text": token.text,
                "type": token.type,
                "display_name": _get_display_name(token.type),
            }
        )

    return tokens


def _get_display_name(tokenType: int) -> str:
    # The generated antlr parser doesn't seem to provide a Vocabulary API out of the box
    vocabulary = {
        JackParser.CLASS: "CLASS",
        JackParser.CONSTRUCTOR: "CONSTRUCTOR",
        JackParser.FUNCTION: "FUNCTION",
        JackParser.METHOD: "METHOD",
        JackParser.FIELD: "FIELD",
        JackParser.STATIC: "STATIC",
        JackParser.VAR: "VAR",
        JackParser.INT: "INT",
        JackParser.CHAR: "CHAR",
        JackParser.BOOLEAN: "BOOLEAN",
        JackParser.VOID: "VOID",
        JackParser.TRUE: "TRUE",
        JackParser.FALSE: "FALSE",
        JackParser.NULL: "NULL",
        JackParser.THIS: "THIS",
        JackParser.LET: "LET",
        JackParser.DO: "DO",
        JackParser.IF: "IF",
        JackParser.ELSE: "ELSE",
        JackParser.WHILE: "WHILE",
        JackParser.RETURN: "RETURN",
        JackParser.LBRACE: "LBRACE",
        JackParser.RBRACE: "RBRACE",
        JackParser.LPAREN: "LPAREN",
        JackParser.RPAREN: "RPAREN",
        JackParser.LBRACK: "LBRACK",
        JackParser.RBRACK: "RBRACK",
        JackParser.DOT: "DOT",
        JackParser.COMMA: "COMMA",
        JackParser.SEMI: "SEMI",
        JackParser.ADD: "ADD",
        JackParser.SUB: "SUB",
        JackParser.MUL: "MUL",
        JackParser.DIV: "DIV",
        JackParser.AND: "AND",
        JackParser.OR: "OR",
        JackParser.LT: "LT",
        JackParser.GT: "GT",
        JackParser.EQ: "EQ",
        JackParser.NOT: "NOT",
        JackParser.INTEGER: "INTEGER",
        JackParser.STRING: "STRING",
        JackParser.IDENTIFIER: "IDENTIFIER",
        JackParser.API_COMMENT: "API_COMMENT",
        JackParser.COMMENT: "COMMENT",
        JackParser.LINE_COMMENT: "LINE_COMMENT",
        JackParser.WS: "WS",
    }

    return vocabulary[tokenType].lower()
