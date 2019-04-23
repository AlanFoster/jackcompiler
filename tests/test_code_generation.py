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


def test_handle_simple_assignment():
    source = """
        class Main {
           function void main() {
              var int x;
              var int y;
              var int z;

              let x = 2;
              let y = 4;
              let z = x + y;

              return;
           }
        }
     """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 3\n"
        "push constant 2\n"
        "pop local 0\n"
        "push constant 4\n"
        "pop local 1\n"
        "push local 0\n"
        "push local 1\n"
        "add\n"
        "pop local 2\n"
        "push constant 0\n"
        "return\n"
    )
