import pathlib

import pkg_resources
from config import author, author_email, description, name, release, repo
from setuptools import find_packages, setup


def readme():
    with open("README.rst") as f:
        return f.read()


# 3rd-party run-time requirements:
with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    author=author,
    author_email=author_email,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    data_files=[
        ("", ["AUTHORS.rst", "CHANGELOG.rst", "LICENSE", "README.rst"])
    ],
    description=description,
    include_package_data=True,
    install_requires=install_requires,
    keywords=[
        "immutable",
        "python",
        "type system",
    ],
    license="MIT",
    long_description=readme(),
    name=name,
    package_data={
        name: ["py.typed"],
    },
    packages=find_packages(),
    python_requires=">=3.8.7",
    url=repo,
    version=release,
    zip_safe=False,
)
