# Haxian Toy Language 

Welcome to the Haxian Interpreter!

## Introduction
Haxian is a simple interpreted language designed for learning and experimentation. This document provides a reference for its syntax and features.

## Basic Syntax
- **Numbers:** Integers and floating-point numbers are supported. Example: `42`, `3.14`
- **Operators:**
  - Addition: `+`
  - Subtraction: `-`
  - Multiplication: `*`
  - Division: `/`
  - Power: `^`
  - Modulo: `%`
  - Equality: `==`
  - Less/Greater Than: `<`, `>`
- **Parentheses:** Use `(` and `)` to group expressions. Example: `(1 + 2) * 3`
- **Variables:** Coming soon
- **Functions:** Coming soon

## Example Usage
```
haxian> 1 + 2 * 3
7
haxian> (4 + 5) / 3
3.0
haxian> 2 ^ 3
8
haxianr> 10 % 3
1
```

## Error Handling
- Invalid characters or syntax will result in a descriptive error message with file, line, and column information.
- Arithmetic errors such as division by zero are caught and reported.
- File operation errors (e.g., file not found) are handled gracefully.

## Arithmetic Evaluation
The interpreter now supports full arithmetic expression evaluation with proper operator precedence:
1. Parentheses have the highest precedence
2. Exponentiation (^) is evaluated next
3. Multiplication (*), division (/), and modulo (%) are evaluated next
4. Addition (+) and subtraction (-) have the lowest precedence
5. Comparison operators (==, <, >) have lower precedence than arithmetic operators


## Getting Started
1. Run the interpreter with `python shell.py`.
2. Enter your Haxian expressions at the prompt.
3. View results or error messages instantly.
4. To execute a Haxian script file, enter the filename with the .hax extension.

---

## TODO / Changelog
- [X] Develop Lexer for Haxian language
- [X] Implement Token module for token representation
- [X] Create interactive shell (shell.py) for REPL experience
- [X] Implement arithmetic expression evaluation
- [X] Add support for power (^) and modulo (%) operators
- [X] Fix bugs in Lexer (null checks and token handling)
- [X] Improve error handling for file operations and expressions
- [X] Add comparison operators
- [ ] Add support for variables and assignments
- [ ] Implement function calls and definitions
- [ ] Add array and object support
- [ ] Expand error handling and reporting
- [ ] Implement control flow statements (if/else, loops)

---

Haxian

---

Enjoy exploring the Haxian language!
