# Python Distributions

[A][1] package distribution can be defined as the collection of files that together allows to build, package and distribute a module. Once a distribution exists in a system, it can easily be installed. Also, it can be shared with PyPI(Python package index) community so that other people can use your distribution.

[There are][3] two types of [distributions][2]:

- **Source Distribution (sdist)**: A source distributions is the simpler of the two types of distributions. Intuitively speaking, an sdist is very similar to source code - the code that you write. Therefore, sdist will not include platform-specific binaries. The result is an archive (.tar.gz) that contains the source code of your package and instructions on how to build it, and the target system of your client will perform the actual build to create a bdist (wheel).

  Creating an sdist is akin to sharing just the source. It doesn't build usable artifacts that the client can consume immediately. The advantage of this is that creating an sdist is the same for all platforms (Windows, Linux, Mac) and machines (32 Bit / 64 Bit). The disadvantage is that users have to build the package themselves once they download the sdist.

- **Built Distribution (bdist)**: It creates distribution which includes .pyc files(python bytecode), .so/.dll/.dylib for binary modules, .exe if using [pyinstaller](https://pyinstaller.org/en/stable/) on Windows, data files… but no `setup.py`. The result is an archive that is specific to a platform (for example linux-x86_64) and to a version of Python. That can be installed and then used directly by extracting it into the root of your filesystem (executables are in `/usr/bin` (or equivalent), data files in `/usr/share`, modules in `/usr/lib/pythonX.X/site-packages/…`).


# Taks

### Virtual environments

A software that creates isolated environments in which a Python package and its dependences are installed and run.

### Project dependency management

A software that
- Adds or Removes packages dependency on a dependency file (such as `pyproject.toml`) of the project.
- Writes on a file (such as `poetry.lock`) the version of all packages required to run the python project.
- Installs those package dependencies in their specific versions. It is usually done within a isolated environment. When the sofware is run on another system, the version of the dependencies is "locked" to those versions listed in `poetry.lock` to ensure reproducibility.
> NOTE: [An](https://www.youtube.com/watch?v=QX_Nhu1zhlg&t=193s) example of how not having package manager can mess things up.

### [Packaging (AKA publishing)](https://youtu.be/QX_Nhu1zhlg?t=433)

The process of building a Python distribution and uploading it on a online software repository (such as PyPI).

### Package management

A software that
- Downloads and installs Python packages which were published in a package index registry, such as PyPI, and make them system- or user-wide callable.
- Downloads and installs all the package dependencies that the wanted package needs. Some package managers provide mechanisms for creating isolated or virtual environments to install them.
- Installs a package at a specific version, if it is required.
- Uninstalls a previously installed package.

# Tools

> WARNING: virtual environments, python dependency management, packaging, and package manager aren't separated tasks, and many tools try to tackle some of them simutaneously.

| Tool | Year | Virtual env | Project dependency | Packaging | Package manager | Comments |
| ---  | :---:  | :---:    | :---: | :---:       | :---:    |  --- |
| Anaconda and [`conda`](https://github.com/conda/conda) | ??? | ✅ | ✅ | :x: | ✅ | [Contains](https://youtu.be/3J02sec99RM?t=156) its own package manager, `conda`; [Limited](https://youtu.be/-QSUyDvHQGY?t=50) number of available packages; `pip` can be used within a `conda` virtual environment, but `conda` cannot handle the packages installed by `pip`; tailored for scientific applications; [removes](https://youtu.be/-QSUyDvHQGY?t=143) both the package and its dependencies; [doesn't](https://youtu.be/-QSUyDvHQGY?t=155) lock files; doesn't separate production and development dependencies within the same file. `environment.yml` and `environment-dev.yml` are used instead. |
| `distutils`/[`setuptools`](https://github.com/pypa/setuptools) | 2000/2004 | :x: | ✅ | ✅ | :x: | `distutils` is a module available since Python 1.6 that provides a basic infrastructure for packaging Python modules and distributing them, but lacks some advanced features; `setuptools` is a third-party library that builds on top of `distutils` and enhances its functionality. Although it was a popular tool for packaging Python libraries in the past, `setuptools` may be considered obsolete for some developers; [To](https://youtu.be/pA4XriRWVxQ?t=281) actually publish your Python library, you need to use another package `twine`|
| [`virtualenv`](https://github.com/pypa/virtualenv) | 2007 | ✅ | :x: | :x: | :x: | Standard Python environments; often used with `pip` for dependency management |
| `pip` | 2008 | :x: | ✅ | :x: | ✅ | Default Python package manager; used with `virtualenv` for isolated environments; PyPI is the default package index; [doesn't](https://youtu.be/-QSUyDvHQGY?t=132) uninstall the dependency packages; [locks](https://youtu.be/-QSUyDvHQGY?t=200) dependencies with the `requirements.txt` file, but requires manual modifications, which is error-prone; [doesn't](https://youtu.be/-QSUyDvHQGY?t=317) separate production and development dependency within the same file. `requirements.txt` and `requirements-dev.txt` are used instead; [To](https://youtu.be/pA4XriRWVxQ?t=411) update the `requirements.txt` from the current installed packages, you can run `pip freeze > requirements.txt`; general-purpose package installer for both libraries and apps with no environment isolation |
| [`pipx`](https://github.com/pypa/pipx) | 2019 |   ✅ | ✅ | :x: | ✅ | help you install and run end-user applications written in Python; closely related to pip. In fact, it uses pip, but is focused on installing and managing Python packages that can be run from the command line directly as applications; adds isolation yet still makes the apps available in your shell: `pipx` creates an isolated environment for each application and its associated packages; `pipx` does not replace `pip` or virtual environments. For normal Python development, use virtual environments and pip or use a tool like Poetry. What pipx provides is isolation and convenience. `pipx` can be used to install any Python package with executables that you want to access from the command line, system-wide.|
| `pipenv` | 2017 | ✅ | ✅ |  ✅ | ✅ | [Can](https://youtu.be/3J02sec99RM?t=170) be used used to manave other vitual environments, such as `virtualenv` and Anaconda; Has hability to decide which virtual env must be enabled when entering in a directory.  |
| `venv` | Python Standard Library (Python 3.3+) | ✅ | ✅ | :x: | :x: | Standard library module for creating virtual environments |
| `pyvenv` | Python 3.3 - 3.6 | ✅ | ✅ | :x: | :x: | Script for creating virtual environments; replaced by `venv` in later Python versions |
| `poetry` | 2018 |  |  |  |  | [Locks](https://youtu.be/-QSUyDvHQGY?t=245) the dependency with the `poetry.lock` file, which is automatically updated when wanted; [contains](https://youtu.be/-QSUyDvHQGY?t=339) both development and production dependencies within the same file (`pyproject.toml`) |

## Conclusions

The utimate conclusion is:
- We have a trillion tools that is intended to solve these issues.
- When it comes to project dependency management, packaging, and virtual environments, Poetry is the way-to-go.
- To install Python applications, use `pipx` [as][4] it provides packages isolations. 
- Honorable mentions to
  - `setuptools`: had been became a standard tool for building up a Python distribution. Nowadays, it may be consedered obsolete by some, though;
  - `pip`: is the default package manager to install packages from PyPI or elsewhere. Although it doesn't provide package isolation, it is still widely used and can easilly be adoped instead of `pipx`.
  - `conda`: a good package manager tailored to scientific applications.
  - `pipenv`: is the Poetry's main competitor as `pipenv` can manage multiple Python version, which is not possible with Poetry(?). `pipenv` is also largely used in my Python projects.

# Examples

### setuptools/distutils

TODO:
https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages

### poetry


[1]: https://www.geeksforgeeks.org/source-distribution-and-built-distribution-in-python/
[2]: https://youtu.be/QX_Nhu1zhlg?t=352&si=OOcG9cDoCnnzCYBE
[3]: https://dev.to/icncsx/python-packaging-sdist-vs-bdist-5ekb
[4]: https://dev.to/bowmanjd/how-do-i-install-a-python-command-line-tool-or-script-hint-pipx-3i2
