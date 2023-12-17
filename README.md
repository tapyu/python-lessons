# Python packages

- A Python package is a directory structure containing Python codes which perform a specific set of functionalities.
- Packages can contain sub-packages and modules (`.py` files), forming a nested structure.
- In addition to sub-packages and modules, a Python package also contains files related to [package managenment and versioning](https://github.com/tapyu/python-lessons/tree/package-managers).

## A typical Python package structure

```
.
├── pypackage
│   ├── config.py
│   ├── gui.py
│   ├── __init__.py
│   ├── __main__.py
│   └── parse_xls.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## The `__init__.py` file

- Each Python package (directory) contains a special `__init__.py` file (which can be empty) to indicate that this directory should be treated as a package.
- The `__init__.py` file in a Python package serves as the initialization code for the package, and it is executed when the package is imported, that is, `import pypackage`. The main purpose of this file is to set up the package and expose specific functionalities or symbols to the external world when the package is imported. It servers as a the "package's API".
- As of Python 3.3 and later, it is not strictly necessary to include an `__init__.py` file in the root directory of your project to consider it a package. In modern Python, implicit namespace packages are supported, which means you can have a directory structure without the need for an `__init__.py` file at every level. However, if you're working with older versions of Python (before 3.3) or if you want to ensure compatibility with tools and practices that expect the presence of `__init__.py` files, you might still include it.

## The `__main__.py` file

- `__main__.py` allows you to define a main entry point for your Python package when it is run as a module, that is, `python -m pypackage`. This command works only if:
    1. The file `pypackage/__main__.py` exists.
    2. You are in the parent directory of `pypackage` or if the path to `pypackage` is searchable by `python`.
-  It provides a way to structure your package for script execution, defining behaviors specific to running the package from the command line.

## Running your Python package

### Local run

1. If you are in the parent directory of `pypackage/`, you can run the Python script `__main__.py` from the terminal using the following command:
```sh
python pypackage/__main__.py
```
1. Alternatively, you can navigate into the `pypackage/` directory and then run the script:
```sh
cd pypackage
python __main__.py
```
1. If you want to run the project from the directory right above `pypackage/`, you can use the `-m` switch to run the the `__main__.py` module:
```sh
python -m pypackage.__main__
```
1. You can also run the `pypackage` package as a module (that is, as a Python script file) by running
```sh
python -m my_package
```
When you run a package as a module, Python first looks for the `__init__.py` file in the package `mypackage`, its code is executed when the package is imported and this file is optional for Python versions 3.3 or later. This file is meant for package initialization and can include any setup code that should run when the package is imported.

After the initialization, the `__main__.py` file is executed if the package is run as a script using the `-m` option. The code in `__main__.py` typically contains the main entry point for the script or module. The `__main__.py` usually contains
```py
if __name__ == "__main__":
    main()
```
`__name__` is a special variable (usually called "dunder variable") in Python that is automatically set by the interpreter. When a Python script is executed, the `__name__` variable is set to `"__main__"` if the script is the main program being run.  This block checks if the package is being executed as the main program (and not imported as a module). When you run `python -m pypackage`, the `__name__` attribute is set to `"__main__"` as the main file run is `pypackage\__main__.py`.

While it's true that variables and imports within `__init__.py` are not automatically available outside its scope, the main purpose of this file is to set up the package and expose specific functionalities or symbols to the external world when the package is imported. For instance, You can use `__init__.py` to import modules or symbols that should be available when the package is imported. This can help users easily access commonly used components of the package.
```py
# NOTE: in __init__.py
from .module1 import some_function
from .module2 import another_function
```
Now, when someone imports the package (`import pypackage`), they can directly access `some_function` and `another_function`.

NOTE: Files, variables, and methods such as `__main__.py`, `__name__`, and `__new__()` are called dunder files, variables, and methods, respectively.

# Python modules

- In contrast to creating Python packages, you can create a single Python file, that is, a Python module.

Example of a simple module (see `my_module.py`):
```py
#!/usr/bin/env python

def my_function(i):
    print(f"Hello from my_function in my_module: {i}")

variable_in_module = 42
my_function(variable_in_module)
```
With the shebang `#!/usr/bin/env python` and by allowing execution permission, you can simply type `/path/to/my_module.py` to run this Python script. If you don't put the shebang, you can also type
```sh
python ./my_module.py
```
or
```sh
python -m my_module
```
to run it.

## `__all__` variable

The `__all__` variable in a Python file is used to define what symbols (functions, classes, or variables) should be considered as part of:
- A package's "public API": When you declare the `__all__` variable in the `__init__.py` file of a Python package, something like
```py
__all__ = [
    "a_variable_name",
    "another_variable_name",
    "a_method_name",
    "a_class_name"
]
```
and someone imports this package using the `from package_name import *` syntax, only those variables, classes, and methods defined in `__all__` will be imported.
- A module (that is, a `.py` file): It works in the very same way, that is, when someone uses the syntax `from my_package.my_module import *` those variables, classes, and methods defined in `__all__` will be imported.
