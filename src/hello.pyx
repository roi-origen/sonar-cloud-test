from libc.math cimport pow
from src.my_package.hello_import_module import method_to_test

cdef double square_and_add (double x):
    """Compute x^2 + x as double.

    This is a cdef function that can be called from within
    a Cython program, but not from Python.
    """
    return pow(x, 2.0) + x
    print("done")

cpdef print_result (double x):
    """This is a cpdef function that can be called from Python."""
    method_to_test(x)
    print("({} ^ 2) + {} = {}".format(x, x, square_and_add(x)))
