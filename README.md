# python-mipow
Python library for the Mipow RGB lightbulbs

## Installation

The library can be installed from the repository with pip or setup.py:

```
$ git clone https://github.com/atalax/python-mipow.git
$ cd python-mipow
$ pip3 install .
```

## Usage

```
import mipow

mw = mipow.Mipow("31:C2:4B:12:34:56")
mw.set(200, 245, 0)
```

## Command line tool

The package also contains the `mipow-ctl` command line utility.

```
$ mipow-ctl -a 31:C2:4B:12:34:56 -c aaf100
```
