# Python - Environment & First Programs

## Introduction & Context

Python can execute code in two primary ways:

- Interactively, using the interpreter (REPL)
- By executing a script file

Professional software development requires understanding both execution modes, how tools are installed, and how environments influence behavior.

This project builds a structured mental model of:

- How the interpreter evaluates expressions and statements
- How a script differs from interactive execution
- How development tools are installed using `pip`
- Why global installations can create conflicts
- How virtual environments isolate dependencies

---

## Learning Objectives

By the end of this project, you should be able to:

- Distinguish between expressions and statements in the interpreter
- Predict when output appears automatically in interactive mode
- Create a portable, executable Python script
- Install and use development tools via `pip`
- Explain the difference between global installations and isolated environments
- Demonstrate dependency isolation using `venv`

---

## Resources

- Python Tutorial — Using the Interpreter  
  https://docs.python.org/3/tutorial/interpreter.html

- Python Standard Library — venv  
  https://docs.python.org/3/library/venv.html

- pip User Guide (overview)  
  https://pip.pypa.io/en/stable/user_guide/

- pycodestyle documentation  
  https://pycodestyle.pycqa.org/

---

## General Requirements

- All code is executed on **Ubuntu 20.04 LTS**
- Python version: **3.8.x**
- Every Python file must start with:

```bash
#!/usr/bin/env python3

Files must be:
Executable
End with a newline
PEP8 compliant (pycodestyle 2.7.x)
Output must match exactly the expected format
No external libraries are allowed unless explicitly stated

## Project Goal

This directory focuses on:

Understanding Python execution modes
Writing first executable scripts
Using proper environment setup practices
Ensuring clean, standardized Python code

