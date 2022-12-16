## How to Create Python Package

two complusory files
- __init__.py
- setup.py

`__init__.py`: import module-name this file will execute.

`setup.py`: execute when `pip install <...>`

```python3
import setuptools

# code here

setuptools.setup(name='Pyname', description='testing python package')
```

to build python package
```
python3 setup.py sdist
```

**ignore warnings**

change directory to dist
`cd dist`

to upload on [PyPI](www.pypi.org)

create a account or login if already created.

on terminal,
```
sudo pip3 install twine
twine upload  ...tar.gz
# fill the username and passwd


pip install module-name 
```
