## Implementations

Programming languages can have multiple implementations. Different implementations can be written in different languages and can use different methods to compile or interpret [code][1]. In Python, when people talk about Python implementations, they usually refer to different runtime environments or interpreters that execute Python code. These implementations may have different features, performance characteristics, and use cases.

- **CPython**: [CPython][2] is the *reference implementation* of the Python programming language ([reference][4] implementation is a program that implements all requirements from a corresponding specification. The reference implementation often accompanies a technical standard, and demonstrates what should be considered the "correct" behavior of any other implementation of it). Written in C and Python, CPython is the default and most widely used implementation of the Python language. On you computer, if `python` is linked to `python3.x`, where `x` is a version number (e.g., `python3.10`), it's CPython. [It][3] compiles Python programs into an intermediate bytecode which is then executed by its virtual machine. It has a foreign function interface with several languages, including C, in which one must explicitly write bindings in a language other than Python.
- **MicroPython**: MicroPython is a software implementation of a programming language largely compatible with Python 3, written in C, that is optimized to run on a microcontroller. MicroPython does have an inline assembler, and that code will run at full speed, but it's non-portable across different microcontrollers (as any assembly is).
- **CircuitPython**: [is][9] an open-source derivative of the MicroPython programming language targeted toward students and beginners. Development of CircuitPython is supported by Adafruit Industries. It is a software implementation of the Python 3 programming language, written in C. It has been ported to run on several modern microcontrollers.


## Subset

A subset of a programming language is a smaller, restricted version of the language that includes only a specific set of features, constructs, or functionalities. In Python, we have

- **Cython**: [It][6] is a programming language which aims to simplify writing C and C++ extension modules for the CPython Python runtime. [It][2] is a subset of the programming language Python, which allows developers to write Python code (with optional, C-inspired syntax extensions) that yields performance comparable to that of C. [The][5] resulting code is also usable with Python via direct C-level API calls into the Python interpreter.

## JIT Compilers

Python is generally considered an interpreted language, and its standard implementation, CPython, uses an interpreter to execute Python code. However, there are tools and technologies that provide a form of compilation or optimization for Python code. 

- **PyPy**: [is][7] an implementation of the Python programming language. PyPy often runs faster than the standard implementation CPython because PyPy uses a just-in-time (JIT) compiler. Most Python code runs well on PyPy except for code that depends on CPython extensions, which either does not work or incurs some overhead when run in PyPy. 
- **Numba**: [is][10] an open-source JIT compiler that translates a subset of Python and NumPy into fast machine code using LLVM, via the llvmlite Python package. It offers a range of options for parallelising Python code for CPUs and GPUs, often with only minor code changes.

Numba and PyPy both use Just-In-Time (JIT) compilation techniques, but they have different focuses and approaches.

PyPy:
- PyPy is a complete alternative implementation of Python. It includes a JIT compiler that translates Python bytecode into machine code at runtime.
- PyPy aims to provide improved performance for a wide range of Python programs by using a JIT compiler.

Numba:
- Numba is a specialized JIT compiler primarily designed for numerical code and scientific computing in Python.
- It translates Python functions into machine code at runtime, focusing on accelerating numerical computations.
- Numba is often used in scenarios where performance is critical for numerical algorithms, and it provides decorators (`@jit`) to specify which functions should be compiled.

In summary, while both PyPy and Numba utilize JIT compilation, PyPy is a general-purpose Python interpreter with a focus on overall performance improvement, while Numba is specifically designed for numerical computations, providing a way to accelerate certain types of code in Python.

---

## Transpilers

A transpiler, short for source-to-source compiler, is a type of compiler that translates source code from one programming language into the equivalent source code in another programming language. Unlike traditional compilers that translate source code into machine code or an intermediate representation, a transpiler generates source code that is intended to be read and understood by humans. In Python, we have:

- [Nuitka][11]: [Nuitka][12] is a source-to-source compiler which compiles Python code to C source code, applying some compile-time optimizations in the process such as constant folding and propagation, built-in call prediction, type inference, and conditional statement execution.
- [MyHDL][13]: is a Python-based hardware description language (HDL), that converts MyHDL code to Verilog or VHDL code.


---

[1]: https://en.wikipedia.org/wiki/Programming_language_implementation#Multiple_implementations
[2]: https://en.wikipedia.org/wiki/CPython
[3]: https://en.wikipedia.org/wiki/Python_(programming_language)#Implementations
[4]: https://en.wikipedia.org/wiki/Reference_implementation
[5]: https://en.wikipedia.org/wiki/Python_(programming_language)#Cross-compilers_to_other_languages
[6]: https://en.wikipedia.org/wiki/List_of_Python_software#Python_implementations
[7]: https://en.wikipedia.org/wiki/PyPy
[8]: https://en.wikipedia.org/wiki/MicroPython
[9]: https://en.wikipedia.org/wiki/CircuitPython
[10]: https://en.wikipedia.org/wiki/Numba
[11]: https://nuitka.net/doc/user-manual.html
[12]: https://en.wikipedia.org/wiki/Nuitka
[13]: https://www.myhdl.org/
