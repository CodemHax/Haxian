# Haxian Language Reference

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
- **Parentheses:** Use `(` and `)` to group expressions. Example: `(1 + 2) * 3`

## Example Usage
```
haxian > 1 + 2 * 3
7
haxian > (4 + 5) / 3
3.0
```

## Error Handling
- Invalid characters or syntax will result in a descriptive error message with file, line, and column information.

## Getting Started
1. Run the interpreter with `python shell.py`.
2. Enter your Haxian expressions at the prompt.
3. View results or error messages instantly.

---

## TODO / Changelog
- [X] Develop Lexer for Haxian language
- [X] Implement Token module for token representation
- [X] Create interactive shell (shell.py) for REPL experience
- [ ] Add support for variables and assignments
- [ ] Expand error handling and reporting
- [ ] Add more operators and language features

---

Haxian

---

Enjoy exploring the Haxian language!
