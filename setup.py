import pathlib

import pkg_resources
from setuptools import setup

# 3rd-party run-time requirements:
with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(install_requires=install_requires)
