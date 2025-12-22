#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "python-box<8",
]

extras = {
    "deploy": ["wheel", "twine"],
    "etcd": ["python-etcd"],
    "develop": ["isort", "watchdog"],
    "docs": ["sphinx", "sphinx_rtd_theme"],
    "k8s": ["kubernetes"],
    ':python_version<"3.6"': ["watchdog<1"],
    ':python_version>"3.6"': ["watchdog>1"],
    "test": [
        "codecov",
        "coverage",
        "flake8",
        "funcsigs",
        "kubernetes",
        "mock",
        "pytest",
        "pytest-lazy-fixtures",
        "pytest-cov",
        "pytest-runner",
        "python-etcd",
        "ruamel.yaml>=0.15",
        "tox",
    ],
    "yaml": ["ruamel.yaml>=0.15"],
}

setup(
    name="yapconf",
    version="0.5.0",
    description="Yet Another Python Configuration",
    long_description=readme + "\n\n" + history,
    author="The Beer Garden Team + Logan Asher Jones",
    author_email="beer@beer-garden.io",
    url="https://github.com/beer-garden/yapconf",
    packages=find_packages(include=["yapconf"]),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords="yapconf",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    test_suite="tests",
    tests_require=extras["test"],
    extras_require=extras,
)
