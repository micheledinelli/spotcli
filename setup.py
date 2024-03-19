from setuptools import find_packages
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

MAJOR_VERSION = '0'
MINOR_VERSION = '0'
MICRO_VERSION = '1'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

setup(name='spotcli',
      version=VERSION,
      description="Cli tool to use spotify from terminal",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Dinelli Michele',
      url='https://github.com/micheledinelli/spotcli',
      author_email='dinellimichele00@gmail.com',
      install_requires=[
          'spotipy',
      ],
      entry_points={
          'console_scripts': ['spotcli = spotcli.__main__:main']
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Customer Service',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software Distribution',
          'Topic :: Utilities'
      ],
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      platforms='any')
