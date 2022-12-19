## Arguments Parsing

In CLI, mostly program support arguments, it make quick to input data in one line command.

create a program which accepts data input in one-line,

> you used sys module also or optparse is same.
> function are little bit different, argparse is updated.

we will use module name `argparse` here.
 

```python
# import argparse module
import argparse
```
argparse is in-build module, to take input data 
arguments, 
**types of arguments**
- positional
- optional

positional arguments requie ti be filled,
and optional are not.

```
parser = argparse.ArgumentParser()
parser.add_argument('--f', '--file', type=str, default='default', help='help will appear')
args = parser.parse_args()
print(args)
```
