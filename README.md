# A typical Python structure

```
my_project/
├── __init__.py
├── __main__.py
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── README.md
```

- In a Python project, the main entry point (`__main__.py`) is typically a script or a module that is executed when the program is run.

## Package vs. Module

- A module is a single Python file containing Python code. It serves as a way to organize Python code, allowing you to encapsulate related functionality into a single file. Modules can define functions, classes, and variables, which can be used by other modules or scripts.

Example of a simple module (`my_module.py`):
```py
def my_function():
    print("Hello from my_function in my_module")

variable_in_module = 42
```

- A package is a way of organizing related modules into a directory hierarchy. It contains a special `__init__.py` file (which can be empty) to indicate that the directory should be treated as a package. Packages can contain sub-packages and modules, forming a nested structure.

Example of a simple package:
```
my_package/
├── __init__.py
├── module1.py
└── module2.py
```
- The `__init__.py` file can be empty or can contain package-level initialization code, that is,  code that is executed when the package is imported. As of Python 3.3 and later, it is not strictly necessary to include an `__init__.py` file in the root directory of your project to consider it a package. In modern Python, implicit namespace packages are supported, which means you can have a directory structure without the need for an `__init__.py` file at every level. However, if you're working with older versions of Python (before 3.3) or if you want to ensure compatibility with tools and practices that expect the presence of `__init__.py` files, you might still include it.

## Running your Python project

1. If you are in the parent directory of `my_project/`, you can run the Python script `__main__.py` from the terminal using the following command:
```sh
python my_project/__main__.py
```
1. Alternatively, you can navigate into the `my_project/` directory and then run the script:
```sh
cd my_project
python __main__.py
```
1. If you want to run the project from the directory right above `my_project/`, you can use the `-m` switch to run the the `__main__.py` module:
```sh
python -m my_project.__main__
```
1. You can also run the `my_project` package as a module (that is, as a Python script file) by running
```sh
python -m my_package
```
When you run a package as a module, Python first looks for the `__init__.py` file in the package `mypackage`, its code is executed when the package is imported and this file is optional for Python versions 3.3 or later. This file is meant for package initialization and can include any setup code that should run when the package is imported.

After the initialization, the `__main__.py` file is executed if the package is run as a script using the `-m` option. The code in `__main__.py` typically contains the main entry point for the script or module. The `__main__.py` usually contains
```py
if __name__ == "__main__":
    main()
```
`__name__` is a special variable (usually called "dunder variable") in Python that is automatically set by the interpreter. When a Python script is executed, the `__name__` variable is set to `"__main__"` if the script is the main program being run.  This block checks if the package is being executed as the main program (and not imported as a module). When you run `python -m my_project`, the `__name__` attribute is set to `"__main__"` as the main file run is `my_project\__main__.py`.

NOTE: Files, variables, and methods such as `__main__.py`, `__name__`, and `__new__()` are called dunder files, variables, and methods, respectively.

## Importing a package; `__all__` variable