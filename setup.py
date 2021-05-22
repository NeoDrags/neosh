from os import name
from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name = "yash-shell",
    packages = find_packages(),
    version = "0.0.1",
    description = "Yet Another SHell but written in python",
    long_description = README,
    long_description_content_type = "text/markdown",
    url="https://github.com/neodrags/yash-shell",
    author="Prateek Kesavarapu",
    author_email="kesavarapu.prateek@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["prompt-toolkit", "termcolor", "pygments"],
    entry_points = {
        "console_scripts": [
            "yash = __main__:main"
        ]
    }
)