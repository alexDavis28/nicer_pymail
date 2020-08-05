from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE.txt") as f:
    license = f.read()

setup(
    name="nicer_pymail",
    version='0.2.0',
    description='Python package to make interfacing with email systems (mostly gmail) easier',
    long_description=readme,
    author='justsomeonenamedalex',
    url='https://github.com/justsomeonenamedalex/nicer_pymail',
    license=license,
    packages=["nicer_pymail"]
)