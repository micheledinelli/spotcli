# setup.py
from setuptools import setup, find_packages

try:
   import pypandoc
   long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
   long_description = open('README.md').read()


setup(
    name='spotycli-package',
    version='0.1.0',

    long_description_content_type="text/markdown",

    long_description=long_description,

    packages=find_packages(),
    install_requires=[
        'typer',
        'spotipy',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'spotycli = main:app',
        ],
    },
)
