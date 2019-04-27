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
           function void main() {
              do Output.printInt(Main.add(5, -10);
              return;
           }

           function int add(int x, int y) {
              var int answer;
              let answer = x + y;
              return answer;
           }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        # Main function
        "function Main.main 0\n"
        "push constant 5\n"
        "push constant 10\n"
        "neg\n"
        "call Main.add 2\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        "push constant 0\n"
        "return\n"
        # Add function
        "function Main.add 1\n"
        "push argument 0\n"
        "push argument 1\n"
        "add\n"
        "pop local 0\n"
        "push local 0\n"
        "return\n"
    )


def test_constructor():
    source = """
        class Point {
            field int x;
            field int y;

            constructor Point new(int xLocation, int yLocation) {
                let x = xLocation;
                let y = yLocation;
                return this;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Point.new 0\n"
        # Allocate memory for two local variables and update the `this` pointer
        "push constant 2\n"
        "call Memory.alloc 1\n"
        "pop pointer 0\n"
        # let x = xLocation
        "push argument 0\n"
        "pop this 0\n"
        # let y = yLocation
        "push argument 1\n"
        "pop this 1\n"
        # Return this pointer
        "push pointer 0\n"
        "return\n"
    )


def test_setter_method():
    source = """
        class Point {
            field int x;
            field int y;

            constructor Point new(int xLocation, int yLocation) {
                let x = xLocation;
                let y = yLocation;
                return this;
            }

            method void setX(int newX) {
                let x = newX;
                return;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        # ---------------
        # constructor
        # ---------------
        "function Point.new 0\n"
        # Allocate memory for two local variables and update the `this` pointer
        "push constant 2\n"
        "call Memory.alloc 1\n"
        "pop pointer 0\n"
        # let x = xLocation
        "push argument 0\n"
        "pop this 0\n"
        # let y = yLocation
        "push argument 1\n"
        "pop this 1\n"
        # Return this pointer
        "push pointer 0\n"
        "return\n"
        # ---------------
        # setX method
        # ---------------
        "function Point.setX 0\n"
        # set THIS value to argument 0
        "push argument 0\n"
        "pop pointer 0\n"
        # let x = newX;
        "push argument 1\n"
        "pop this 0\n"
        # return
        "push constant 0\n"
        "return\n"
    )


def test_getter_method():
    source = """
        class Point {
            field int x;
            field int y;

            constructor Point new(int xLocation, int yLocation) {
                let x = xLocation;
                let y = yLocation;
                return this;
            }

            method int getX() {
                return x;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        # ---------------
        # constructor
        # ---------------
        "function Point.new 0\n"
        # Allocate memory for two local variables and update the `this` pointer
        "push constant 2\n"
        "call Memory.alloc 1\n"
        "pop pointer 0\n"
        # let x = xLocation
        "push argument 0\n"
        "pop this 0\n"
        # let y = yLocation
        "push argument 1\n"
        "pop this 1\n"
        # Return this pointer
        "push pointer 0\n"
        "return\n"
        # ---------------
        # getX method
        # ---------------
        "function Point.getX 0\n"
        # set THIS value to argument 0
        "push argument 0\n"
        "pop pointer 0\n"
        # return x;
        "push this 0\n"
        "return\n"
    )


def test_implicit_object_calls():
    source = """
        class Point {
            field int x;
            field int y;

            constructor Point new(int xLocation, int yLocation) {
                let x = xLocation;
                let y = yLocation;
                return this;
            }

            method int getDoubleX() {
                return getX() + getX();
            }

            method int getX() {
                return x;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        # ---------------
        # constructor
        # ---------------
        "function Point.new 0\n"
        # Allocate memory for two local variables and update the `this` pointer
        "push constant 2\n"
        "call Memory.alloc 1\n"
        "pop pointer 0\n"
        # let x = xLocation
        "push argument 0\n"
        "pop this 0\n"
        # let y = yLocation
        "push argument 1\n"
        "pop this 1\n"
        # Return this pointer
        "push pointer 0\n"
        "return\n"
        # ---------------
        # getDoubleX method
        # ---------------
        "function Point.getDoubleX 0\n"
        # set THIS value to argument 0
        "push argument 0\n"
        "pop pointer 0\n"
        # return getX() + getX()
        "push pointer 0\n"
        "call Point.getX 1\n"
        "push pointer 0\n"
        "call Point.getX 1\n"
        "add\n"
        "return\n"
        # ---------------
        # getX method
        # ---------------
        "function Point.getX 0\n"
        # set THIS value to argument 0
        "push argument 0\n"
        "pop pointer 0\n"
        # return x;
        "push this 0\n"
        "return\n"
    )


def test_object_creation():
    source = """
        class Main {
            function void main() {
                var Point point1;
                let point1 = Point.new(2, 3);
                do Output.printInt(point1.getLength());
                return;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 1\n"
        # let point = Point.new(2,3)
        "push constant 2\n"
        "push constant 3\n"
        "call Point.new 2\n"
        # Store the pointer given to us
        "pop local 0\n"
        # do Output.printInt(point.getLength())
        "push local 0\n"
        "call Point.getLength 1\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        # return
        "push constant 0\n"
        "return\n"
    )


def test_arrays():
    source = """
        class Main {
            function void main() {
                var Array array;
                let array = Array.new(2);
                let array[0] = 15;
                let array[1] = 30;
                do Output.printInt(array[0]);
                do Output.printInt(array[1]);
                return;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 1\n"
        "push constant 2\n"
        "call Array.new 1\n"
        # Store the pointer given to us
        "pop local 0\n"
        # array[0] = 15
        "push local 0\n"
        "push constant 0\n"
        "add\n"
        "push constant 15\n"
        "pop temp 0\n"
        "pop pointer 1\n"
        "push temp 0\n"
        "pop that 0\n"
        # array[1] = 30
        "push local 0\n"
        "push constant 1\n"
        "add\n"
        "push constant 30\n"
        "pop temp 0\n"
        "pop pointer 1\n"
        "push temp 0\n"
        "pop that 0\n"
        # do Output.printInt(array[0]);
        "push local 0\n"
        "push constant 0\n"
        "add\n"
        "pop pointer 1\n"
        "push that 0\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        # do Output.printInt(array[1]);
        "push local 0\n"
        "push constant 1\n"
        "add\n"
        "pop pointer 1\n"
        "push that 0\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        # return
        "push constant 0\n"
        "return\n"
    )


def test_array_assignment_from_array():
    source = """
        class Main {
            function void main() {
                var Array array;
                let array = null;
                let array = Array.new(2);
                let array[0] = 15;
                let array[1] = 30;
                let array[0] = array[0] + array[1];
                do Output.printInt(array[0]);
                do Output.printInt(array[1]);
                return;
            }
        }
    """

    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 1\n"
        # array = null
        "push constant 0\n"
        "pop local 0\n"
        # Create new 2 element array
        "push constant 2\n"
        "call Array.new 1\n"
        # Store the pointer given to us
        "pop local 0\n"
        # array[0] = 15
        "push local 0\n"
        "push constant 0\n"
        "add\n"
        "push constant 15\n"
        "pop temp 0\n"
        "pop pointer 1\n"
        "push temp 0\n"
        "pop that 0\n"
        # array[1] = 30
        "push local 0\n"
        "push constant 1\n"
        "add\n"
        "push constant 30\n"
        "pop temp 0\n"
        "pop pointer 1\n"
        "push temp 0\n"
        "pop that 0\n"
        # Starting:  array[0] = array[0] + array[1]
        "push local 0\n"
        "push constant 0\n"
        "add\n"
        # Lookup array[0]
        "push local 0\n"
        "push constant 0\n"
        "add\n"
        "pop pointer 1\n"
        "push that 0\n"
        # lookup array[1]
        "push local 0\n"
        "push constant 1\n"
        "add\n"
        "pop pointer 1\n"
        "push that 0\n"
        # Adding, and storing
        "add\n"
        "pop temp 0\n"
        "pop pointer 1\n"
        "push temp 0\n"
        "pop that 0\n"
        # do Output.printInt(array[0]);
        "push local 0\n"
        "push constant 0\n"
        "add\n"
        "pop pointer 1\n"
        "push that 0\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        # do Output.printInt(array[1]);
        "push local 0\n"
        "push constant 1\n"
        "add\n"
        "pop pointer 1\n"
        "push that 0\n"
        "call Output.printInt 1\n"
        "pop temp 0\n"
        # return
        "push constant 0\n"
        "return\n"
    )


def test_strings():
    source = """
        class Main {
            function void main() {
                do Output.printString("hello world");
                return;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function Main.main 0\n"
        "push constant 11\n"
        "call String.new 1\n"
        "push constant 104\n"
        "call String.appendChar 2\n"
        "push constant 101\n"
        "call String.appendChar 2\n"
        "push constant 108\n"
        "call String.appendChar 2\n"
        "push constant 108\n"
        "call String.appendChar 2\n"
        "push constant 111\n"
        "call String.appendChar 2\n"
        "push constant 32\n"
        "call String.appendChar 2\n"
        "push constant 119\n"
        "call String.appendChar 2\n"
        "push constant 111\n"
        "call String.appendChar 2\n"
        "push constant 114\n"
        "call String.appendChar 2\n"
        "push constant 108\n"
        "call String.appendChar 2\n"
        "push constant 100\n"
        "call String.appendChar 2\n"
        "call Output.printString 1\n"
        "pop temp 0\n"
        "push constant 0\n"
        "return\n"
    )


def test_statics():
    source = """
        class ScreenConstant {
            static int width;
            static int height;

            function void init() {
                let width = 512;
                let height = 255;
                return;
            }

            function int getWidth() {
                return width;
            }

            function int getHeight() {
                return height;
            }
        }
    """
    result = compiler.generate(antlr4.InputStream(source))

    assert result == (
        "function ScreenConstant.init 0\n"
        "push constant 512\n"
        "pop static 0\n"
        "push constant 255\n"
        "pop static 1\n"
        "push constant 0\n"
        "return\n"
        "function ScreenConstant.getWidth 0\n"
        "push static 0\n"
        "return\n"
        "function ScreenConstant.getHeight 0\n"
        "push static 1\n"
        "return\n"
    )
