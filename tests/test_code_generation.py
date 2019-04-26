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


def test_handle_simple_if_statement():
    source = """
        class Main {
           function void main() {
              if (true) {
                do Output.printInt(1);
              }

              return;
           }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 0\n"
        "push constant 0\n"
        "not\n"
        "not\n"
        "if-goto IF_END.2\n"
        "push constant 1\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        "label IF_END.2\n"
        "push constant 0\n"
        "return\n"
    )


def test_handle_simple_if_else_statement():
    source = """
        class Main {
           function void main() {
              if (true) {
                do Output.printInt(1);
              } else {
                do Output.printInt(0);
              }

              return;
           }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 0\n"
        "push constant 0\n"
        "not\n"
        "not\n"
        "if-goto IF_ELSE.1\n"
        "push constant 1\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        "goto IF_END.2\n"
        "label IF_ELSE.1\n"
        "push constant 0\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        "label IF_END.2\n"
        "push constant 0\n"
        "return\n"
    )


def test_handle_simple_while_loop():
    source = """
        class Main {
           function void main() {
              var int x;

              let x = 0;

              while (x < 10) {
                let x = x + 1;
                do Output.printInt(x);
                do Output.println();
              }

              return;
           }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 1\n"
        # x = 0
        "push constant 0\n"
        "pop local 0\n"
        # while (x < 10) {
        "label LOOP_START.1\n"
        "push local 0\n"
        "push constant 10\n"
        "lt\n"
        "not\n"
        "if-goto LOOP_END.2\n"
        # let x = x + 1
        "push local 0\n"
        "push constant 1\n"
        "add\n"
        "pop local 0\n"
        # do Output.printInt(x)
        "push local 0\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        # do Output.println()
        "call Output.println 0\n"
        "pop temp 0\n"
        "goto LOOP_START.1\n"
        # }
        "label LOOP_END.2\n"
        # return
        "push constant 0\n"
        "return\n"
    )


def test_function_with_arguments():
    source = """
        class Main {
           function int add(int x, int y) {
              var int answer;
              let answer = x + y;
              return answer;
           }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.add 1\n"
        "push argument 0\n"
        "push argument 1\n"
        "add\n"
        "pop local 0\n"
        "push local 0\n"
        "return\n"
    )
