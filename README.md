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

| Tool | Year | Virtual environments | Project dependency | Packaging | Package management |
| ---  | :---:  | :---:                   | :---:                | :---:       | :---:                |
| `setuptools` | 2004 | :x: | ✔ | :x: | ✔️ |

## Conclusions

The utimate conclusion is:
- We have a trillion tools that is intended to solve these issues.
- When it comes to project dependency management, packaging, and virtual environments, Poetry is the way-to-go.
  > Warning: Poetry is not intended to be a package manager! You should use `pip` or `pipx` instead.
- Honorable mentions to
  - `setuptools`: had been became a standard tool for building up a Python distribution. Nowadays, it may be consedered obsolete by some, though;
  - `PyPI` (Python Package Index): has become the official third-party software repository for Python. However, it has nothing to do with the package dependency, packaging, and creating virtual environments;
  - `pip`: has become the default package manager to install packages from PyPI or elsewhere.
  - `conda`: a good package manager tailored to scientific applications.
 
## Advantage of Poetry over the other tools

- It wonderfully does the script install in the `[tool.poetry.scripts]` section. It was usually done by `setuptools` and `setup.py`.

### setuptools

TODO:

https://stackoverflow.com/questions/77664095/what-are-the-differences-between-pipx-and-pip-user

https://trello.com/c/66EaMW4j/86-general-knowledge-except-errors-and-warnings-pkg-mng-and-virtenv-packaging

https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko

https://dev.to/bowmanjd/how-do-i-install-a-python-command-line-tool-or-script-hint-pipx-3i2

https://www.reddit.com/r/learnpython/comments/jq5miv/pip_vs_pipx/

https://github.com/pypa/pipx

https://stackoverflow.com/questions/59286983/how-to-run-a-script-using-pyproject-toml-settings-and-poetry

https://ericmjl.github.io/blog/2016/12/24/how-to-make-your-python-scripts-callable-from-the-command-line/

https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages


[1]: https://www.geeksforgeeks.org/source-distribution-and-built-distribution-in-python/
[2]: https://youtu.be/QX_Nhu1zhlg?t=352&si=OOcG9cDoCnnzCYBE
[3]: https://dev.to/icncsx/python-packaging-sdist-vs-bdist-5ekb
