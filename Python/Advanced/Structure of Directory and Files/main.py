# Importing Classes and function

# import func1.py # unsafe
# from func1 import * # unsafe

# import Class Func and other function func2()
from file1 import Func, func2

# directory1 import file func2.py from it import Class Func2 and other function func4()
from directory1.file2 import Func2, func4

# from directory2 file file3 import Class Func3 and its function create obj using Func3.func5()
#from directory2.file3 import Func3

# w/ __init__.py
# import directory2 all files
# from directory2 import *
# from directory2 import file3, file4

# Without w/o __init__.py
# directory 2 file func3 and 4 import Class Func3 and 4 and functions func6() and func8
from directory2.file3 import Func3, func6
from directory2.file4 import Func4, func8

print("\n main.py: Running file file1.py from class Func function func1")
Func.func1()

print("\n main.py: Running file file1.py function func2")
func2()

print("\n main.py: Running from directory1: file file2.py: class Func3 function func3().")
Func2.func3()

print("\n main.py: Running from directory1: file file2.py: function func4().")
func4()

print("\n main.py: Running from directory2: file file3.py: class Func3: function func5().")
Func3.func5()

print("\n main.py: Running from directory2: file file3.py function func6().")
func6()

print("\n main.py: Running from directory2: file file4.py: class Func4: function func7().")
Func4.func7()

print("\n main.py: Running from directory2: file file4.py function func8().")
func8()