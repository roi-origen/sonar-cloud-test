import os
import pyximport
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
from pathlib import Path
pyximport.install()

ext_modules = [
    Extension(name=".".join(path.parts).rstrip(".pyx"), sources=[str(path)], include_dirs=["."])
    for path in Path('src').rglob('*.pyx')
]

setup(
    ext_modules=cythonize(ext_modules),
)

for path in Path('src').rglob('*.c'):
    os.remove(path)

# python setup.py build_ext --inplace
