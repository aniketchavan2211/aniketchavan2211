### Structure of Directory and Files

1. `import` modules

```python3
import module_name
module.func()
```

2. using `from ... import ...`

```python3
from module import class/function

# directly run function
func() 
```

3. import all

```python3
# imports all classes and functions
from module import *

```

4. `as` keyword 

```python3
# use to alias 
from module import func as f

f()
```

5. Checks module 

```python3
print(dir(module))
```

structure
```
--> main.py
--> file1.py
--> directory1 --> file2.py --> Func2 class --> func3()
                            --> func4()
--> directory2 --> __init__.py 
               --> file3.py --> Func3 class --> func5()
                            --> func6()
               --> file4.py --> Func4 class --> func7()
                            --> func8()
```