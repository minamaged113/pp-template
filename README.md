[![Ubuntu support](https://img.shields.io/static/v1?label=ubuntu&message=18.04&color=green&style=for-the-badge&logo=ubuntu)](http://releases.ubuntu.com/18.04.4/)
[![Python support](https://img.shields.io/static/v1?label=Python&message=3.6&color=blue&style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-360/)
[![Contact information](https://img.shields.io/static/v1?label=Contact%20me&message=email&color=blue&style=for-the-badge&logo=microsoftoutlook)](mailto:minamaged113@gmail.com?subject=PP-Template&body=Hello%20Mina%2C%0AThis%20message%20is%20regarding%20Python%20Project%20Template%20scripts.%0A%0ABest%20regards.%0A%3CYOUR_NAME%3E)
[![Request feature](https://img.shields.io/static/v1?label=Request&message=Feature&color=blue&style=for-the-badge&logo=addthis)](https://github.com/minamaged113/pp-template/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=)
[![Report bug](https://img.shields.io/static/v1?label=Report&message=bug&color=blue&style=for-the-badge)](https://github.com/minamaged113/pp-template/issues/new?assignees=&labels=bug&template=bug_report.md&title=)
[![CircleCI Build Status](https://img.shields.io/circleci/build/github/minamaged113/pp-template/master?color=blue&label=MASTER%20BUILD&logo=circleci&style=for-the-badge&token=33be814517fadea414e106e538711f002bbcefa7)](https://app.circleci.com/pipelines/github/minamaged113/pp-template)

# Project Template

This repository is intended to be a project template. Fork it to your own repository and start developing.

## Start it

```bash
git clone https://github.com/minamaged113/pp-template.git
cd pp-template
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Package it

```bash
python3 setup.py sdist bdist_wheel
```

## Upload it

In order to distribute your work as a package, you should link your code, development environment, and CI environment to publishing host.

### PYPI Account

You should have an account on the **PY**thon **P**ackaging **I**ndex. Create your account [here](https://pypi.org/account/register/) or [login](https://pypi.org/account/login/) to an existing account.

### PYPI Production Token

Create a token for your account on the production environment to allow publishing packages without password from [here](https://pypi.org/manage/account/token/).

### Staging Environment

If you want, you can create a staging environment, where you can push pre-release packages. PyPI provides a testing package index which can provide you with the needed hosting platform. Visit [Test PyPI](https://test.pypi.org/) for more information. 

You should be able to perform the last 2 steps exactly the same again to the staging environment in Test PyPI.

### Configuration file 

To define your configuration for the python package indexes, create a `.pypirc` file. If you are using linux, this file is usually found in `$HOME/.pypirc`. If it is not there, create it and populate it with the following:

```bash
[pypi]
  username = __token__
  password = <PLACE_YOUR_TOKEN_HERE>
```

If you have congigured your own staging environment, you can add it to the `.pypirc` file also, as follows:

```bash
[testpypi]
  username = __token__
  password = <PLACE_YOUR_TEST_TOKEN_HERE>
```

After configuring the `.pypirc` file, go ahead and restrict access to it, because saving information as text, unencrypted, is not the brightest idea.

```bash
chmod 600 $HOME/.pypirc
```


## READ MORE

1. https://packaging.python.org/specifications/pypirc/
2. 