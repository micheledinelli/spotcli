# setup.py
from setuptools import setup, find_packages

try:
   import pypandoc
   long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
   long_description = open('README.md').read()

setup(
    name='spotcli',
    version='{{VERSION_PLACEHOLDER}}',
    author="micheledinelli",
    author_email="dinellimichele00@gmail.com",

    long_description_content_type="text/markdown",

    long_description=long_description,

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typer',
        'spotipy',
        'python-dotenv',
        'halo',
        'inquirer',
        'Pygments',
    ],
    entry_points={
        'console_scripts': [
            'spoticli = spoticli.main:app',
        ],
    },
)
