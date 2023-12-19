# Python Distributions

[A][1] package distribution can be defined as the collection of files that together allows to build, package and distribute a module. Once a distribution exists in a system, it can easily be installed. Also, it can be shared with PyPI(Python package index) community so that other people can use your distribution.

[There are][3] two types of [distributions][2]:

- **Source Distribution (sdist)**: A source distributions is the simpler of the two types of distributions. Intuitively speaking, an sdist is very similar to source code - the code that you write. Therefore, sdist will not include platform-specific binaries. The result is an archive (.tar.gz) that contains the source code of your package and instructions on how to build it, and the target system of your client will perform the actual build to create a bdist (wheel).

  Creating an sdist is akin to sharing just the source. It doesn't build usable artifacts that the client can consume immediately. The advantage of this is that creating an sdist is the same for all platforms (Windows, Linux, Mac) and machines (32 Bit / 64 Bit). The disadvantage is that users have to build the package themselves once they download the sdist.

- **Built Distribution (bdist)**: It creates distribution which includes .pyc files(python bytecode), .so/.dll/.dylib for binary modules, .exe if using [pyinstaller](https://pyinstaller.org/en/stable/) on Windows, data files… but no `setup.py`. The result is an archive that is specific to a platform (for example linux-x86_64) and to a version of Python. That can be installed and then used directly by extracting it into the root of your filesystem (executables are in `/usr/bin` (or equivalent), data files in `/usr/share`, modules in `/usr/lib/pythonX.X/site-packages/…`).


# Tasks
> WARNING: These tasks do not refer to specific Python packages or external software. Rather, it refers to functionalities that one desires throughout the development or production (as an end user) phases.

### Virtual environments

A software that
- Creates isolated environments in which a Python package and its dependences are installed and run.
- Is frequently used by both Python developers and end users, whether to isolate package dependencies to safely run Python projects or to isolate the installed dependencies of each Python package.

### Project dependency management

A software that
- Adds or Removes packages dependency on a dependency file (such as `pyproject.toml`) of the project.
- Writes on a file (such as `poetry.lock`) the version of all packages required to run the Python project.
- Installs package dependencies in their required versions. It is usually done within a isolated environment. When the sofware is run on another system, the version of the dependencies is "locked" to those versions listed in `poetry.lock` to ensure reproducibility.
- Is required only by Python developers.
> NOTE: [An](https://www.youtube.com/watch?v=QX_Nhu1zhlg&t=193s) example of how not having dependency manager can mess things up.

### Packaging (AKA publishing)

[A](https://youtu.be/QX_Nhu1zhlg?t=433) software that
- Builds a Python distribution and uploading it on a online software repository (such as PyPI).
- Is required only by Python developers.

### Package management

A software that
- Installs Python packages which is either downloaded from a remote package index, such as PyPI, or availabe on the [local machine][6].
- Make the installed Python packages system- or user-wide callable by creating shell scripts in `$PATH`.
- Downloads and installs all the package dependencies that the desired package needs.
- Solves version conflicts between the packages' dependencies. Some package managers, like `pipx`, provide mechanisms for creating virtual environments to isolate the dependencies of each installed Python package.
- Installs a package at a specific version, if it is required.
- Uninstalls a previously installed package (and its dependencies).
- Is usually required by end users.

# Tools

> WARNING: virtual environments, dependency management, packaging, and package management aren't separated tasks. Many tools try to tackle some of them simutaneously.

### Anaconda and [`conda`](https://github.com/conda/conda)

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| ??? | ✅ | ✅ | :x: | ✅ |

- [Contains](https://youtu.be/3J02sec99RM?t=156) its own package manager, `conda`.
- [Limited](https://youtu.be/-QSUyDvHQGY?t=50) number of available packages.
- `pip` can be used within a `conda` virtual environment, but `conda` cannot handle the packages installed by `pip`.
- Tailored for scientific applications
- [Removes](https://youtu.be/-QSUyDvHQGY?t=143) both the package and its dependencies.
- [Doesn't](https://youtu.be/-QSUyDvHQGY?t=155) lock files
- Doesn't separate production and development dependencies within the same file. `environment.yml` and `environment-dev.yml` are used instead.

### `distutils`/[`setuptools`](https://github.com/pypa/setuptools)/`twine`

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| 2000/2004 | :x: | ✅ | ✅ | :x: |

- `distutils` is a module available since Python 1.6 that provides a basic infrastructure for packaging Python modules and distributing them, but lacks some advanced features.
- `setuptools` is a third-party library that builds on top of `distutils` and enhances its functionality.
- Although it was a popular tool for publishing and locally installing Python libraries in the past, `setuptools` may be considered obsolete for some developers.
- [To](https://youtu.be/pA4XriRWVxQ?t=281) actually publish your Python library, you need to use another package `twine`.
- Other usual files associated whith this approach are `setup.py`, `setup.cfg`, and `MANIFEST.in`.

### [`virtualenv`](https://github.com/pypa/virtualenv)

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| 2007 | ✅ | :x: | :x: | :x: |

- Standard Python virtual environments.
- Often used with `pip` for dependency management.

### `pip`

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| 2008 | :x: | ✅ | :x: | ✅ |

- Default Python package manager; used with `virtualenv` for isolated environments.
- PyPI is the default package index; [doesn't](https://youtu.be/-QSUyDvHQGY?t=132) uninstall the dependency packages.
- [Locks](https://youtu.be/-QSUyDvHQGY?t=200) dependencies with the `requirements.txt` file, but requires manual modifications, which is error-prone.
- [Doesn't](https://youtu.be/-QSUyDvHQGY?t=317) separate production and development dependency within the same file. `requirements.txt` and `requirements-dev.txt` are used instead.
- [To](https://youtu.be/pA4XriRWVxQ?t=411) update the `requirements.txt` from the current installed packages, you can run `pip freeze > requirements.txt`.
- General-purpose package installer for both libraries and apps with no environment isolation.

### [`pipx`](https://github.com/pypa/pipx)

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| 2019 |   ✅ | ✅ | :x: | ✅ |

- Install and runs end-user applications written in Python.
- Closely related to pip. In fact, it uses pip, but is focused on installing and managing Python packages that can be run from the command line directly as applications.
- Adds isolation yet still makes the apps available in your shell: `pipx` creates an isolated environment for each application and its associated packages.
- `pipx` does not replace `pip` or virtual environments. For normal Python development, use virtual environments and `pip` or use a tool like Poetry.
- What pipx provides is isolation and convenience. `pipx` can be used to install any Python package with executables that you want to access from the command line, system-wide.

### `pipenv`

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| 2017 | ✅ | ✅ |  ✅ | :x: |
- [Can](https://youtu.be/3J02sec99RM?t=170) be used used to manave other vitual environments, such as `virtualenv` and Anaconda.
- Has hability to decide which virtual env must be enabled when entering in a directory.

### `venv`

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
 | Python Standard Library (Python 3.3+) | ✅ | ✅ | :x: | :x: |

### `pyvenv`

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| Python 3.3 - 3.6 | ✅ | ✅ | :x: | :x: |

- Replaced by `venv` in later Python versions (?).

### `poetry`

| Year | Virtual env | Project dependency | Packaging | Package manager |
| :---:  | :---:    | :---: | :---:       | :---:    |
| 2018 | ✅ | ✅ | ✅ | :x: |

- [Locks](https://youtu.be/-QSUyDvHQGY?t=245) the dependency with the `poetry.lock` file, which is automatically updated when wanted.
- [Contains](https://youtu.be/-QSUyDvHQGY?t=339) both development and production dependencies within the same file (`pyproject.toml`).
- Package managers, such as `pip` and `pipx`, can use `poetry.lock` and `pyproject.toml` to [locally install][6] the current Python project

# Conclusions

The utimate conclusions are:
- We have a trillion tools that is intended to solve these issues.
- When it comes to project dependency management, packaging, and virtual environments, Poetry is the way-to-go.
- Use `pipx` to install Python applications (that is, for end users) [as][4] it provides packages isolations.
- Since `pipx` is used for Python package management and `poetry` for project dependency management, packaging, and virtual environments, there is no need to use `pip` anymore.
- Honorable mentions to
  - [`distutils`/`setuptools`][5]: had become a standard tool for building up Python distributions, in the past. Nowadays, it may be considered obsolete by some, though;
  - `pip`: is the default PyPI's package manager. Although it doesn't provide virtual environments to isolate each installed Python package, it is still widely used and is not considered obsolete. A common application of `pip` is its usage along with virtual environment for dependency management. This functionality, however, can be easier performed by `poetry`, nowadays.
  - `conda`: a good package manager tailored to scientific applications.
  - `pipenv`: One might consider using it over `poetry` as the former provides Python interpreter isolation, whereas the latter doesn't (?). `pipenv` is also largely used in many Python projects.


[1]: https://www.geeksforgeeks.org/source-distribution-and-built-distribution-in-python/
[2]: https://youtu.be/QX_Nhu1zhlg?t=352&si=OOcG9cDoCnnzCYBE
[3]: https://dev.to/icncsx/python-packaging-sdist-vs-bdist-5ekb
[4]: https://dev.to/bowmanjd/how-do-i-install-a-python-command-line-tool-or-script-hint-pipx-3i2
[5]: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages
[6]: https://github.com/tapyu/python-lessons/tree/dir-structure?tab=readme-ov-file#local-installation-of-the-python-project-via-a-packager-manager
