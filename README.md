# Python packages (AKA libraries)

- [A Python package][1] is a directory structure containing Python codes which perform a specific set of functionalities.
- Packages can contain sub-packages and modules (`.py` files), forming a nested structure.
- In addition to sub-packages and modules, a Python package also contains files related to [dependency managenment and versioning](https://github.com/tapyu/python-lessons/tree/package-managers).

## A typical Python package structure
> NOTE: This Python project uses `poetry` for dependency management, but [other tools][2] can also be used for this purpose.

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
- The `__init__.py` file in a Python package serves as the initialization code for the package, and it is executed when the package is imported, that is, `import pypackage`. For instance, on the Python REPL:
  ```
  >>> import pypackage
  >>> pypackage
  <module 'pypackage' from '/path/to/pypackage/__init__.py'>
  ```
  Although `requests` is a package (i.e., a directory), importing it actually imports `/path/to/pypackage/__init__.py`, which is a module (i.e., a `.py` file). Therefore, the main purpose of `__init__.py` is to set up the package and expose specific functionalities or symbols to the external world when the package is imported. In other words, it servers as a the "package's API".
- In `__init__.py`, you can import other modules, functions, and variables that should be available once the package is imported. This can help users easily access commonly used components of the package. For instance:
    ```py
    # NOTE: in __init__.py
    from .module1 import some_function
    from .module2 import another_function
    ```
    Now, when someone imports the package (`import pypackage`), they can directly access `some_function` and `another_function`, for example, `pypackage.some_function()`.
- As of Python 3.3 and later, it is not strictly necessary to include an `__init__.py` file in the root directory of your project to consider it a package. In modern Python, implicit namespace packages are supported, which means you can have a directory structure without needing an `__init__.py` file in every level. However, if you're working with older versions of Python (before 3.3) or if you want to ensure compatibility with tools and practices that expect the presence of `__init__.py` files, you might still include it.

## The `__main__.py` file

- `__main__.py` allows you to define the entrypoint of your Python package when it is run as a module, that is, `python -m pypackage`. This command works only if:
    1. The file `pypackage/__main__.py` exists.
    2. You are in the parent directory of `pypackage` or if the path to `pypackage` is searchable by `python`.
-  It provides a way to structure your package for script execution, defining specific behaviors when running it from the command line.
-  The `__main__.py` usually contains
    ```py
    if __name__ == "__main__":
        main()
    ```
    `__name__` is a special variable in Python that is automatically set by the interpreter. When a Python package is executed as a module, the `__name__` variable is set to `"__main__"` since it is the main program which is being run.  This block checks if the package is being executed as the main program (and not imported). Therefore, when you run `python -m pypackage`, the `__name__` attribute is set to `"__main__"` as the main file run is `pypackage\__main__.py`.

> NOTE: Files, variables, and methods such as `__main__.py`, `__name__`, and `__new__()` are called dunder files, variables, and methods, respectively. Dunder is an abbreviation for "Double UNDERscore".

## Running a Python package

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

### Global run via the `PYTHONPATH` environment variable

In order to run `my_package` globally (that is, from anywhere), you must set the `PYTHONPATH` environment variable.

- On GNU/Linux, just run
    ```sh
    export PYTHONPATH="/path/to/parent/directory:/path/to/another/parent/directory"
    ```
    where `/path/to/parent/directory` is the parent directory path where `my_package/` is located in.

- On Windows, you need to set a [user environment variables](https://stackoverflow.com/a/4855685/13998346):

  ![](https://i.stack.imgur.com/ZGp36.png)

Now, from any directory on your terminal, you can run
```sh
python -m my_package
```
and `python` will find `my_package` and run it.

Note that you cannot run `my_package` if you put this Python package within one of the directories listed in `$PATH` as Python packages are directories, and directories cannot be executed. [To make a Python package executable, you need to install it](https://github.com/tapyu/python-lessons/blob/package-managers/README.md).

### Local installation of the Python project via a packager manager

In the parent directory of `pypackage/`, tou can run
```sh
pip install pypackage
```
- To install this Python package locally, that is, from the source code in `pypackage/`.
- `pip` uses the information from the `pyproject.toml` and `poetry.lock` files to install your project and its dependencies.
- If the dependencies are not found on your local machine or if their version doesn't match the requirements listed in `pyproject.toml`, `pip` downloads installs the Python packages at the correct version from PyPI.
- In the `pyproject.toml` file, `pip` uses the information
    ```toml
    [tool.poetry.scripts]
    correcao = "pypackage.__main__:main"
    ```
    to generate a callable script, which is stored at `$HOME/.local/bin/correcao` (on GNU/Linux). This file is an executable Python script with the following content
    ```py
    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    import re
    import sys
    from pypackage.__main__ import main
    if __name__ == '__main__':
        sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
        sys.exit(main())
    ```
    In short, this executable Python script run `pypackage.__main__`, where `pypackage` is the Python package which is now located at `$HOME/.local/lib/pythonX.XX/site-packages/`.
- You can use `pipx` instead of `pip`.
- To uninstall it, just run
    ```sh
    pip uninstall pypackage
    ```

# Python modules

- In contrast to creating Python packages, you can create [a single Python file, that is, a Python module][1].

Example of a simple module (see `my_module.py`):
```py
#!/usr/bin/env python

def my_function(i):
    print(f"Hello from my_function in my_module: {i}")

variable_in_module = 42
my_function(variable_in_module)
```

## Running a Python module

### Local run

With the shebang `#!/usr/bin/env python` and by allowing execution permission, you can simply type
```sh
/path/to/my_module.py
```
to run this Python script. If you don't put the shebang, you can also type
```sh
python ./my_module.py
```
or
```sh
python -m my_module
```
to run it.

### Global run (in the `PATH` environment variable)

Alternatively, you can save `my_module.py` within one of the paths listed in the `$PATH` environment variable. In this case, if you put the shebang in `my_module.py` and make it executable, you can simply type:
```py
my_module.py
```
to run this Python script (if you don't want to write the file extension, just save this file as `my_module`. It works in the very same way).

# `__all__` variable

The `__all__` variable in a Python file is used to define what symbols (functions, classes, or variables) should be considered as part of:
- A package's "public API": When you declare the `__all__` variable in the `__init__.py` file of a Python package, e.g.,
```py
__all__ = [
    "a_variable_name",
    "another_variable_name",
    "a_method_name",
    "a_class_name"
]
```
and someone imports this package using the `from package_name import *` syntax, only those variables, classes, and methods defined in `__all__` will be imported.
- A module (that is, a `.py` file): It works in the very same way, that is, when someone uses the syntax `from my_package.my_module import *`, only those variables, classes, and methods defined in `__all__` will be imported.


[1]: https://youtu.be/QX_Nhu1zhlg?t=352&si=OOcG9cDoCnnzCYBE
[2]: https://github.com/tapyu/python-lessons/tree/packaging?tab=readme-ov-file#tools
