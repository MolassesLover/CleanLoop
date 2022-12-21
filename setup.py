import subprocess
import os
from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as readme:
    long_desc = readme.read()

if os.path.exists("src"):
    subprocess.run("mv src clean_loop", shell=True)

setup(
    name="clean-loop",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    description="Repeat a script every given number of seconds",
    author="MolassesLover",
    author_email="60114762+MolassesLover@users.noreply.github.com",
    url="https://github.com/MolassesLover/CleanLoop",
    install_requires=["colorama"],
    license="MIT",
    entry_points={
        "console_scripts": [
            "clean_loop = clean_loop.cli:main",
        ]
    },
)

if os.path.exists("clean_loop"):
    subprocess.run("mv clean_loop src", shell=True)
