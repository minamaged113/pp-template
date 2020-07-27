# This Makefile contains all predefined commands to develop for this
# package.
version:
	@ python3 -c "from src.package_template import __VERSION__; print(__VERSION__)"

package:
	python3 -m pip install --user --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m pip install --user --upgrade twine

clean:
	-rm -rf dist build *.egg-info
	-find . -name '*.pyc' -delete
	-find . -name '*.pyo' -delete
	
lint:
	- pylint src --score=y