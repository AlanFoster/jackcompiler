# Jack Compiler

A compiler written with [ANTLR](https://www.antlr.org/) for the Jack language, a language similar to Java, which will
run on the Hack platform.

## What is it?

Following the through the book `The Elements of Computing Systems`, this project is part of a larger suite of tools:

       +------------+     +-------------+     +------------+
       |    Jack    |     |   Virtual   |     |            |
       |  Compiler  +---->+   Machine   +---->+  Assembler |
       |            |     |  Translator |     |            |
       +------------+     +-------------+     +------------+

### Jack Compiler

The [Jack Compiler](https://github.com/AlanFoster/jackcompiler) converts the high level Jack language into an
intermediate representation which can be ran on a platform agnostic virtual machine. The syntax of Jack is similar to
Java. The virtual machine instructions output by this compiler are stack based, and is modeled after the Java Virtual
Machine (JVM).

This project is written with [ANTLR](https://www.antlr.org/) and Python.

### Hack Virtual Machine Translator

The Jack Compiler outputs virtual machine code. These virtual machine instructions can be compiled using the
[hack virtual machine translator](https://github.com/AlanFoster/hackvirtualmachine). At a high level this tool converts
virtual machine instructions into symbolic assembly commands which can then be passed to an assembler.

This project is written with [ANTLR](https://www.antlr.org/) and Python.

### Hack Assembler

The [Hack Assembler](https://github.com/AlanFoster/hackassembler) takes the symbolic representation of assembly
commands, and converts these instructions into its binary representation using the Hack Assembler. This can then be
loaded on to the Hack platform's ROM and executed.

This project is written with Go.

## Project links

This project is part of a larger suite of tools:

- [Jack Compiler](https://github.com/AlanFoster/jackcompiler) converts the high level Jack language into an
  intermediate representation which can be ran on a platform agnostic virtual machine. Written with [Antlr](https://www.antlr.org/)
  and Python.
- [Hack Virtual Machine Translator](https://github.com/AlanFoster/hackvirtualmachine) - A virtual machine translator
  for the hack assembly language written with [Antlr](https://www.antlr.org/) and Python.
- [Hack Assembler](https://github.com/AlanFoster/hackassembler) - A basic assembler for the Hack symbolic assembly
  language written in Go.

## Supported functionality

The list of instructions includes:

- Object Orientated Programming - Classes, object instantiation, arrays, strings, etc.
- Function calls
- Control Flow - if statements / loops
- Expressions - Including operator precedence
- Variable assignment / lookup

## Examples

Simple expression support with operator precedence:

```java
class Main {
   function void main() {
      do Output.printInt(1 + 2 * 3);
      return;
   }
}
```

The generated "bytecode" output is stack based. Note that Multiplication is an operating system call, as the underlying
hardware does not directly support multiplication.

```assembly
function Main.main 0
push constant 1
push constant 2
push constant 3
call Math.multiply 2
add
call Output.printInt 1
pop temp 0
push constant 0
return
```

## Classes

A class with a simple getter:

```java
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
```

The compiled constructor will make a system call to request enough memory for two fields `x` and `y`. This system call
places the memory location at the top of the stack, and is stored for later use. The symbol table will store the
required information to generate the required segment pointers.

Generated Output - annotated manually:

```assembly
;----------------------------
; constructor
;----------------------------
function Point.new 0
; Allocate memory for two local variables and update the `this` pointer
push constant 2
call Memory.alloc 1
pop pointer 0
; let x = xLocation
push argument 0
pop this 0
; let y = yLocation
push argument 1
pop this 1
; Return this pointer
push pointer 0
return
;----------------------------
; getX method
;----------------------------
function Point.getX 0
; set THIS value to argument 0
push argument 0
pop pointer 0
; return x;
push this 0
return
```

### Strings

The string literal is just syntactic sugar for a `String.new` call with subsequent ascii character appends. There is no
string interning like Java.

```java
class Main {
    function void main() {
        do Output.printString("hello world");
        return;
    }
}
```

Output:

```assembly
function Main.main 0
push constant 11
call String.new 1
push constant 104
call String.appendChar 2
push constant 101
call String.appendChar 2
push constant 108
call String.appendChar 2
push constant 108
call String.appendChar 2
push constant 111
call String.appendChar 2
push constant 32
call String.appendChar 2
push constant 119
call String.appendChar 2
push constant 111
call String.appendChar 2
push constant 114
call String.appendChar 2
push constant 108
call String.appendChar 2
push constant 100
call String.appendChar 2
call Output.printString 1
pop temp 0
push constant 0
return
```

## Notes

### Generate parser

```bash
docker-compose build
docker-compose run --rm service /bin/sh /usr/local/bin/antlr4 Jack.g4 -Dlanguage=Python3 -visitor -o parser
```

Unfortunately the generated method names are camel case, rather than snake case - as shown within the python3 codegen
templates
[here](https://github.com/antlr/antlr4/blob/837aa60e2c4736e242432c2ac93ed2de3b9eff3b/tool/resources/org/antlr/v4/tool/templates/codegen/Python3/Python3.stg#L104)

### Run tests

```bash
docker-compose build
docker-compose run --rm test
```
