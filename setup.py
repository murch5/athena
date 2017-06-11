from distutils.core import setup
from data_manager.__init__ import __version__ as version

setup(
    name='datatypes',
    version=version,
    packages=['data_manager', 'data_manager.datatypes'],
    url='',
    license='',
    author='Ryan',
    author_email='',
    description='Data type classes', requires=['pandas', 'matplotlib']
)
