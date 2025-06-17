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
- **Parentheses:** Use `(` and `)` to group expressions. Example: `(1 + 2) * 3`

## Example Usage
```
interpreter> 1 + 2 * 3
7
interpreter> (4 + 5) / 3
3.0
interpreter> 2 ^ 3
8
interpreter> 10 % 3
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
- [ ] Add support for variables and assignments
- [ ] Expand error handling and reporting
- [ ] Add more operators and language features

---

Haxian

---

Enjoy exploring the Haxian language!