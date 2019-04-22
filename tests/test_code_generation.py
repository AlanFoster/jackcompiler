import antlr4
from compiler import compiler


def test_simple_expression():
    source = """
        class Main {
           function void main() {
              do Output.printInt(1 + (2 * 3));
              return;
           }
        }
     """
    result = compiler.generate(antlr4.InputStream(source))
    assert result == (
        "function Main.main 0\n"
        "push constant 1\n"
        "push constant 2\n"
        "push constant 3\n"
        "call Math.multiply 2\n"
        "add\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        "push constant 0\n"
        "return\n"
    )
