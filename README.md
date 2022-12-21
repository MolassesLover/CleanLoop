# CleanLoop

[![Ko-Fi](https://img.shields.io/badge/donate-kofi-blue?style=for-the-badge&logo=ko-fi&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://ko-fi.com/molasses)
[![Patreon](https://img.shields.io/badge/donate-patreon-blue?style=for-the-badge&logo=patreon&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://www.patreon.com/molasseslover)
[![PyPi](https://img.shields.io/badge/install-pypi-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/clean-loop)

An extremely simple Python script that repeats another script, 
every given number of seconds.

## Usage

In this example, the [`test/test.sh`](https://github.com/MolassesLover/CleanLoop/tree/master/test/test.sh)
script is chosen to loop, with a delay between loops of 
3 seconds.
```sh
➜ python3 src/cli.py --delay 3 --script test/test.sh
```

## Installation

The [`src/cli.py`](https://github.com/MolassesLover/CleanLoop/blob/master/test/test.sh) file can be installed as the
`clean-loop` command using `pip`.

You can install it from [GitHub](https://github.com/MolassesLover/CleanLoop):
```sh
➜ pip install git+https://github.com/MolassesLover/CleanLoop.git
```
Alternatively, from [PyPi](https://pypi.org/project/clean-loop):
```sh
➜ pip install clean-loop
```

## License
All files within this repository are licensed under the 
[Apache v2.0 license](https://github.com/MolassesLover/CleanLoop/blob/master/LICENSE-APACHE.md) or 
[MIT license](https://github.com/MolassesLover/CleanLoop/blob/master/LICENSE-MIT.md) at your choice. 
