import antlr4
from compiler import compiler


def test_lexer_with_empty_input():
    source_code = "class Foo { }"
    result = compiler.lex(antlr4.InputStream(source_code))

    assert result == [
        {"text": "class", "type": 1, "display_name": "class"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "Foo", "type": 43, "display_name": "identifier"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "{", "type": 22, "display_name": "lbrace"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "}", "type": 23, "display_name": "rbrace"},
    ]


def test_lexer_with_basic_class():
    source_code = "class Foo { field int foo; }"
    result = compiler.lex(antlr4.InputStream(source_code))

    assert result == [
        {"text": "class", "type": 1, "display_name": "class"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "Foo", "type": 43, "display_name": "identifier"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "{", "type": 22, "display_name": "lbrace"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "field", "type": 5, "display_name": "field"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "int", "type": 8, "display_name": "int"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "foo", "type": 43, "display_name": "identifier"},
        {"text": ";", "type": 30, "display_name": "semi"},
        {"text": " ", "type": 47, "display_name": "ws"},
        {"text": "}", "type": 23, "display_name": "rbrace"},
    ]
