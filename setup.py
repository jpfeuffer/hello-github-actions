#from Cython.Build import cythonize
from setuptools import setup, Extension

#setup(ext_modules=cythonize(Extension('spam', ['spam.pyx']),
#                            compiler_directives=dict(
#                                language_level='3str', c_string_type='str',
#                                c_string_encoding='utf8')))
setup(ext_modules=[Extension('spam', ['spam.c'])])
