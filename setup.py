from setuptools import setup, find_packages
from src import __VERSION__

setup(
    name="ppt",
    version=__VERSION__,
    # packages=find_packages(exclude=["tests*"]),
    py_modules=["package"],
    package_dir={'': 'src'},
    license="MIT",
    description="Initializes a python project",
    long_description=open("README.md").read(),
    install_requires=[],
    url="https://github.com/minamaged113/pp-template",
    author="Mina Ghobrial",
    author_email="minamaged113@gmail.com",
)