# Geometry Inheritance Project

## Introduction and Context

In many programs, different objects represent variations of the same concept. For example, different geometric shapes may share common characteristics, and different types of users may share similar behavior.

Object-oriented programming allows developers to represent these relationships using **inheritance**.

Inheritance allows a class to reuse and extend behavior from another class. A class that inherits from another class automatically receives its attributes and methods, and it can also modify or extend them.

Another closely related concept is **polymorphism**. Polymorphism allows different objects to respond to the same method call in different ways depending on their class.

Together, inheritance and polymorphism help developers design systems that are easier to maintain, extend, and understand.

In this project, a hierarchy of geometric shapes is created to practice these concepts:

```
BaseGeometry
      │
      ▼
   Rectangle
      │
      ▼
     Square
```

`BaseGeometry` defines common behavior for geometric shapes.  
`Rectangle` inherits from `BaseGeometry` and implements specific rectangle behavior.  
`Square` inherits from `Rectangle` and represents a more specialized shape.

Because `Square` inherits from `Rectangle`, and `Rectangle` inherits from `BaseGeometry`, a `Square` object can also be treated as a `Rectangle` or a `BaseGeometry` object. This relationship demonstrates code reuse and polymorphism.

---

## Learning Objectives

By completing this project, you should be able to:

- Explain how inheritance allows classes to reuse behavior
- Identify parent classes and child classes
- Create subclasses that extend the behavior of another class
- Override inherited methods
- Understand how polymorphism allows objects of different classes to respond to the same method call
- Use `isinstance()` to check object relationships
- Use `issubclass()` to check class relationships
- Design simple inheritance hierarchies

---

## General Requirements

### Environment

- Ubuntu 20.04
- Python 3.8

### Python Files

All Python files must:

- Be executable
- Start with:

```python
#!/usr/bin/env python3
```

- End with a newline

### Coding Rules

- Code must follow PEP 8 style guidelines
- All modules, classes, and functions must include documentation strings
- Only the Python standard library may be used unless otherwise stated
- Do not use the words `import` or `from` inside comments, as the checker may interpret them incorrectly
- To import any base class, use the `__import__()` method

---

## Author

Project completed by Rawan as part of Python Inheritance & Polymorphism for Holberton School.
