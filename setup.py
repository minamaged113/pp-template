from setuptools import setup, find_packages
from src import __VERSION__
import subprocess

def getDependencies(fname):
    """Get dependencies from requirements file.
    Get packages installed by pip inside the virual environment.
    put it in the form of a list
    
    Args:
        fname ([string]): reuirements filename.
    
    Returns:
        dependencyArray ([list]): list of dependendencies for the package
    """
    dependencyArray = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE).stdout.decode('ascii').split('\n')
    return dependencyArray

setup(
    name="ppt",
    version=__VERSION__,
    # packages=find_packages(exclude=["tests*"]),
    py_modules=["package"],
    package_dir={'': 'src'},
    license="MIT",
    description="Initializes a python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    url="https://github.com/minamaged113/pp-template",
    author="Mina Ghobrial",
    author_email="minamaged113@gmail.com",
    classifiers= [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux"
    ]
)