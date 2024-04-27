# spotcli

[![Publish to PyPI](https://github.com/micheledinelli/wifind/actions/workflows/publish-to-pypi.yaml/badge.svg)](https://github.com/micheledinelli/spoticli/actions/workflows/publish-to-pypi.yaml) [![pypi version](https://img.shields.io/pypi/v/spotcli)](https://pypi.org/project/spotcli/) [![pypi downloads](https://img.shields.io/pypi/dw/spotcli)](https://pypi.org/project/spotcli/)

`spotcli` is a cli tool to interact with your spotify account

## Results

`spotcli` is in early stage development. At the moment It supports OAuth2 authentication flow using
[`spotipy` library](https://github.com/spotipy-dev/spotipy)

## Installation

```sh
pip install spotcli
```

## Usage

```
# shows available commands
spotcli --help

spotcli login

spotcli logout
```
