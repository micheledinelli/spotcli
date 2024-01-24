# setup.py
from setuptools import setup, find_packages

setup(
    name='spotycli-package',
    version='0.1.0',
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
