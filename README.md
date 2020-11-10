# HUG
Hug is a Python framework that enables you to interface your code easily.

It supports 3 types of Interfaces:
CLI
HTTP API
Local

Advantages of HUG:
1. Write Once. Use Everywhere.
2. Version Management
3. Auto Documentation
4. Annotation powered Validation

Version Management:
HUG allows you to maintain multiple versions of your API.

Auto Documentation:
Hug creates documentation automatically from Python docstrings and its type annotations.

Annotation powered Validation:
Hug validates input and output for functions based on type annotations. 
It can use:
1. Python’s built-in types
2. Hug’s built-in types
    Hug has some commonly used types. Eg: whole number, UUID, text upto a certain length.
3. Marshmallow types or schemas
    Marshmallow is an object serialization library.
4. Strings
    Used to generate documentation but not validation
Custom Types

In this project I have wrote two scripts, one for HUG CLI and other for HUG API.



