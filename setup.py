# setup.py
from setuptools import setup, find_packages

try:
   import pypandoc
   long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
   long_description = open('README.md').read()

setup(
    name='spoticli-pkg',
    version='0.0.1',
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
    ],
    entry_points={
        'console_scripts': [
            'spoticli = spoticli.main:app',
        ],
    },
)
