## Compiling

```bash
python -m py_compile main.py
```

running using 
```bash
python main.cpython.pyc
```

`pyc` is compile python file


## Decompiling
Install `uncompyle6` is python module to decompile

```
pip install uncompyle6
```

run 
```bash
uncompyle6 main.cpython.pyc > decompilied_python.py
```
