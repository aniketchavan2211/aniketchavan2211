![ Python ](https://github.com/aniketchavan2211/aniketchavan2211/blob/master/Images/python.png)
## Python

### Introduction

#### What is Python?

 Python is a popular programming language. It was created by 
 Guido van Rossum, and released in 1991.

 **It is used for:**
 -  web development (server-side),
 -  software development,
 -  mathematics,
 -  system scripting.

#### What can Python do?

 - Python can be used on a server to create web applications.
 - Python can be used alongside software to create workflows.
 - Python can connect to database systems. It can also read and 
 modify files.
 - Python can be used to handle big data and perform complex 
 mathematics.
 - Python can be used for rapid prototyping, or for production-ready 
 software development.

####  Why Python?

 - Python works on different platforms (Windows, Mac, Linux, 
 Raspberry Pi, etc).
 - Python has a simple syntax similar to the English language.
 - Python has syntax that allows developers to write programs 
 with fewer lines than some other programming languages.
 - Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that 
 prototyping can be very quick.
 - Python can be treated in a procedural way, an object-oriented 
 way or a functional way.

####  Good to know

 - The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
 - In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.
 - Python Syntax compared to other programming languages
 - Python was designed for readability, and has some similarities to the English language with influence from mathematics.
 - Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
 - Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

### Comments 

Comments can be used to explain Python code.
Comments can be used to make the code more readable
Comments can be used to prevent execution when testing code

#### Single-Line Comments

Comments starts with a `#` (hash), amd python
will ignore them :
```python
# This is a Comment
# This is ignore python interpreter
```

Comments can be placed at the end of a line, and Python will ignore the rest of the line
```python
print ("Hello") # This is a comment
```

Output:
```
Hello
```

#### Multi-Line Comments

Python will ignore string literals that are not assigned to a variable, you can add a multiline string ` """ ` (triple quotes) in your code, and 
place your comment inside it.

```python
"""
This is a 
Multi line
Comment
"""
```

### Reserved Keywords
|   |   |   | 
| - | - | - |
| and | exec	| not |
| assert |	finally |	or |
| break	 | for |	pass |
| class	| from	| print |
| continue	| global | raise |
| def	 | if	 | return |
| del |	import | try |
| elif |	in |	while |
| else |	is	| with | 
| except	| lambda | yield |

### Variables

 Variables are containers for storing data values.

 Python has no command for declaring a variable.

 A variable is created the moment you first assign a value to it.

 ```py
 Variable_Name = "Variable_Value"
 # Double Quotes ""
 Variable_Name = 'Variable_Value'
 # Single Quotes ''
 ```

 Variables do not need to be declared with any particular type, and can even change type after they have been set.
 
 If you want to specify the data type of a variable, this can be done with casting.

 ```py
 x = str(3) # x will be string '3'
 y = int(3) # y will be integer 3
 z = float(3) # z will be floating-point number 3.0
 ```

#### Get the Type()

 You can get the data type of a variable with 
 the `type()` function.

 ```py
 # DataType
 string = "value" # str()
 integer = 2 # Don't use quotes for Numbers int()
 float = 2.1 # Don't use quotes for Numbers float()
 boolean = True # bool()
 list = ["A", "B"] # list()
 tuple = ("a", "b") # tuple()
 set = {"C", "D"} # set()
 dictionary = { "key":"value" , "key1":1 } #dict()
 
 print(type(string))
 ```
 
 **Output**:
 ```py 
 <class 'str'> 
 ```
 
#### Datatypes

Variables can store data of different types, and different types can do different things.

| DataTypes |  Types |
| --------- | ------ |
| Text Type |	`str` |
| Numeric Types |	`int`, `float`, `complex`|
| Sequence Types	|`list`, `tuple`, `range`|
| Mapping Type |	`dict`|
| Set Types	|`set`, `frozenset`|
| Boolean Type |`bool`|
| Binary Types|`bytes`, `bytearray`, `memoryview`|

#### Type Conversion

To convert between types, you simply use the type name as a function.

There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

| Function | Description |
| -------- | ----------- |
| int(x [,base]) | Converts x to an integer. base specifies the base if x is a string. |
| long(x [,base] ) | Converts x to a long integer. base specifies the base if x is a string. |
| float(x) | Converts x to a floating-point number. |
| complex(real [,imag]) | Creates a complex number. |
| str(x) | Converts object x to a string representation. |
| repr(x) | Converts object x to an expression string. |
| eval(str) | Evaluates a string and returns an object. |
| tuple(s) | Converts s to a tuple. |
| list(s) | Converts s to a list. |
| set(s) | Converts s to a set. |
| dict(d) | Creates a dictionary. d must be a sequence of (key,value) tuples. |
| frozenset(s) |Converts s to a frozen set. |
| chr(x) | Converts an integer to a character. |
| unichr(x) || Converts an integer to a Unicode character. |
| ord(x) | Converts a single character to its integer value. |
| hex(x) | Converts an integer to a hexadecimal string. |
| oct(x) | Converts an integer to an octal string. |

### User Input / Output
 `input()` function takes input from user and
 stores in Variable.

 `print()` function use to display data(str,int,float,etc)
 on screen or terminal.

 ```py
 Variable = input("Enter your value: ")
 
 print (Variable)
 ```
 **Output**:
 ```py
 "Enter your value: "
 ```

### Operators

Operators are used to perform operations on variable and values.

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

#### Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name	| Example	 |
| -------- | ---- | -------- |
| `+` |	Addition |	x + y	|
|`-`	| Subtraction	| x - y	|
|`*`	| Multiplication |	x * y	|
|`/`|	Division |	x / y	|
|`%`|	Modulus	| x % y	|
|`**`|	Exponentiation |	x ** y	|
|`//`|	Floor division |	x // y|

#### Assignment Operators

Assignment operators are used to assign values to variables

| Operator |	Example |	Same As |
| -------- | -------- | ------  |
|`=`|	x = 5|	x = 5	|
|`+=`	|x += 3|	x = x + 3	|
|`-=`	|x -= 3|	x = x - 3	|
|`*=`	|x *= 3|	x = x * 3	|
|`/=`	|x /= 3|	x = x / 3	|
|`%=`	|x %= 3|x = x % 3|	
|`//=`|x //= 3|x = x // 3	|
|`**=`|x \*\*= 3|	x = x ** 3|	
|`&=`	|x &= 3`|	x = x & 3	|
|`\|=`|	x \|= 3|	x = x \| 3|	
|`^=`	|x ^= 3	|x = x ^ 3	|
|`>>=`|x >>= 3|x = x >> 3	|
|`<<=`|x <<= 3|	x = x << 3|

#### Comparison Operators

Comparison operators are used to compare two values:

| Operator |	Name |	Example |
| -------- | ----- | -------- |
| `==` | Equal	| x == y	|
| `!=`	| Not equal |	x != y	|
| `>` | Greater than	| x > y	|
| `<` | Less than |	x < y	|
| `>=` |	Greater than or equal to	| x >= y	|
| `<= `|	Less than or equal to	 | x <= y |

#### Logical Operators

Logical operators are used to combine conditional statements:

| Operator |Description	| Example	|
| -------- | ---------- | ------- |
| `and` |	Returns True if both statements are true |	x < 5 and |  x < 10	|
| `or` |	Returns True if one of the statements is true |	x < 5 or x < 4	|
| `not` |	Reverse the result, returns False if the result is true	| not(x < 5 and x < 10) |

#### Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator | Description |	Example	|
| -------- | ----------- | -------- |
|`is` | Returns True if both variables are the same object |	x is y |	
| `is not` |	Returns True if both variables are not the same object	| x is not y |

#### Membership Operators

Membership operators are used to test if a sequence is presented in an object:

| Operator |	Description |	Example	|
| -------- | ------------ | -------- |
| `in ` |	Returns True if a sequence with the specified value is present in the object |	x in y |	
|`not in` |	Returns True if a sequence with the specified value is not present in the object |	x not in y |

#### Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

| Operator | Name | Description |
| -------- | ---- | ----------- |
|`&` |	AND|	Sets each bit to 1 if both bits are 1 |
|`\|`	| OR |	Sets each bit to 1 if one of two bits is 1 |
|  `^` |	XOR|	Sets each bit to 1 if only one of two bits is 1 |
| `~` | NOT|	Inverts all the bits |
| `<<` | Zero fill left shift |Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| `>>` |Signed right shift|	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

### Decision Making 

Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions.

Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome. You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.

Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value.

Python programming language provides following types of decision making statements.

#### If statement

The `if` statement contains a logical expression using which data is compared and a decision is made based on the result of the comparison.

**Synatx**
```python
if expression:
statement(s)
```

If the boolean expression evaluates to TRUE, then the block of statement(s) inside the if statement is executed. If boolean expression evaluates to FALSE, then the first set of code after the end of the if statement(s) is executed.

**Example**
```python
var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1
```
**Output**:
```
1 - Got a true expression value
100
```

#### If - Else statement

An else statement can be combined with an if statement. An else statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value.

The else statement is an optional statement and there could be at most only one else statement following if.

**Syntax**
```python
if expression:
statement(s)
else:
statement(s)
```

**Example**
```python
var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1
else:
   print "1 - Got a false expression value"
   print var1
```
**Output**:
```
1 - Got a true expression value
100
```

#### If - Elif - Else statement

The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

Similar to the else, the elif statement is optional. However, unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.

**Syntax**
```python
if expression1:
statement(s)
elif expression2:
statement(s)
elif expression3:
statement(s)
else:
statment (s)
```

**Example**
```python
var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var
```
**Output**:
```
3 - Got a true expression value
100
```

#### Nested - If statement

There may be a situation when you want to check for another condition after a condition resolves to true. In such a situation, you can use the nested if construct.

In a nested if construct, you can have an if...elif...else construct inside another if...elif...else construct.

**Syntax**
```python
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s)
```
**Example**:
```py
var = 100
if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
   elif var == 50:
      print "Which is 50"
   elif var < 50:
      print "Expression value is less than 50"
else:
   print "Could not find true expression"
```
**Output**:
```
Expression value is less than 200
Which is 100
```

### Loops 

A loop statement allows us to execute a statement or group of statements multiple times.

#### While loops

A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.

**Syntax**:
```python
while expression:
   statement(s)
```

**Example**:
```python
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
```

**Output**:
```
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
```

##### Infinite loops

A loop becomes infinite loop if a condition never becomes FALSE.

**Example** :
```python
var = 1
while var == 1 :  # This constructs an infinite loop
   num = ("Enter a number  :")
   print ("You entered : ", num)
```
**Output**:
```
You entered : Entered a number  :
You entered : Entered a number  :
You entered : Entered a number  :
You entered : Entered a number  :
...
```

Loops never ends, And crashed the program

##### Using else Statement with While loops

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

The following example illustrates the combination of an else statement with a while statement that prints a number as long as it is less than 5, otherwise else statement gets executed.

```python
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
```
**Output** :
```
0 is less than 5
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
5 is not less than 5
```

##### On-line While

Similar to the if statement syntax, if your while clause consists only of a single statement, it may be placed on the same line as the while header.

**Example** :
```python
flag = 1
while (flag): print 'Given flag is really true!'
```


#### For loops

If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable iterating_var.

**Syntax**:
```python
for iterating_var in sequence:
   statements(s)
```

**Example**:
```
for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

```
**Output**:
```
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n
Current fruit : banana
Current fruit : apple
Current fruit : mango
```

##### Iterating by Sequence Index

An alternative way of iterating through each item is by index offset into the sequence itself.

**Example**:
```Python
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]
```

**Output**:
```
Current fruit : banana
Current fruit : apple
Current fruit : mango
```

##### Using else Statement with For Loop

If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 10 through 20.

```Python
for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
		break
```

**Output** :
```
10 equals 2 * 5
11 is a prime number
12 equals 2 * 6
13 is a prime number
14 equals 2 * 7
15 equals 3 * 5
16 equals 2 * 8
17 is a prime number
18 equals 2 * 9
19 is a prime number
```


#### Nested Loops

Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept.


**Syntax for For loops** :
```python
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```

**Syntax for while loops** :
```python
while expression:
   while expression:
      statement(s)
   statement(s)
```

**Example** :
```python
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1
```
**Output**:
```
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
29 is prime
31 is prime
37 is prime
41 is prime
43 is prime
47 is prime
53 is prime
59 is prime
61 is prime
67 is prime
71 is prime
73 is prime
79 is prime
83 is prime
89 is prime
97 is prime
```

### Loops Controls

Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.

#### Break statements

It terminates the current loop and resumes execution at the next statement.

The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.

If you are using nested loops, the break statement stops the execution of the innermost loop and start executing the next line of code after the block.

**Syntax** :
```python
break
```

**Example** :
```python
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break
```
**Output** :
```
Current Letter : P
Current Letter : y
Current Letter : t
Current variable value : 10
Current variable value : 9
Current variable value : 8
Current variable value : 7
Current variable value : 6
```

#### Continue statements

It returns the control to the beginning of the while loop.. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.

**Syntax** :
```python
continue
```

**Example** :
```python
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
```

**Output** :
```
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : o
Current Letter : n
Current variable value : 9
Current variable value : 8
Current variable value : 7
Current variable value : 6
Current variable value : 4
Current variable value : 3
Current variable value : 2
Current variable value : 1
Current variable value : 0
```

#### Pass statments

It is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet (e.g., in stubs for example)

**Syntax** :
```python
pass
```

**Example** :
```python
for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter
```

**Output** :
```
Current Letter : P
Current Letter : y
Current Letter : t
This is pass block
Current Letter : h
Current Letter : o
Current Letter : n
```

### Numbers

There are three numeric types in Python:

- `int`
- `float`
- `complex`

Variables of numeric types are created when you assign a value to them:

**Example:**
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

To verify the type of any object in Python, use the `type()` function:

**Example:**
```python
print(type(x))
print(type(y))
print(type(z))
```
**Output:**
```
<class 'int'>
<class 'float'>
<class 'complex'>
```

#### Int

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

**Example:**
Integers:
```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```
**Output:**
```
<class 'int'>
<class 'int'>
<class 'int'>
```

#### Float

Float, or `floating point number` is a number, positive or negative, containing one or more decimals.

**Example:**
Floats:
```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```
**Output
```
<class 'float'>
<class 'float'>
<class 'float'>
```

Float can also be scientific numbers with an "e" to indicate the power of 10.

**Example:**
Floats:
```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```
**Output:**
```
<class 'float'>
<class 'float'>
<class 'float'>
```

#### Complex

Complex numbers are written with a "j" as the imaginary part:

**Example:**
Complex:
```python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```
**Output:**
```
<class 'complex'>
<class 'complex'>
<class 'complex'>
```

#### Type Conversion

You can convert from one type to another with the `int()`, `float()`, and `complex()` methods:

**Example:**
Convert from one type to another:
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```
**Output:**
```
1.0
2
(1+0j)
<class 'float'>
<class 'int'>
<class 'complex'>
```

***`Note`: You cannot convert complex numbers into another number type.***

#### Random Number

Python does not have a `random()` function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers:

**Example:**
Import the random module, and display a random number between 1 and 9:
```python
import random

print(random.randrange(1, 10))
```
**Output:**
```
9
```

### Boolean

Booleans represent one of two values: `True` or `False`
.

#### Boolean Values

In programming you often need to know if an expression is `True` or `False`.

You can evaluate any expression in Python, and get one of two answers, `True` or `False`.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

**Example:**
```python
print(10 > 9)
print(10 == 9)
print(10 < 9)
```
**Output:**
```
True
False
False
```

When you run a condition in an if statement, Python returns `True` or `False`:

**Example:**

Print a message based on whether the condition is `True` or `False`:
```python
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```
**Output:**
```
b is not greater than a
```

#### Evaluate Values and Variables

The `bool()` function allows you to evaluate any value, and give you `True` or `False` in return,

**Example:**

Evaluate a string and a number:
```python
print(bool("Hello"))
print(bool(15))
```
**Output:**
```
True
True
```

**Example:**

Evaluate two variables:
```python
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
```
**Output:**
```
True
True
```

#### Most Values are True

Almost any value is evaluated to `True` if it has some sort of content.

Any string is `True`, except empty strings.

Any number is `True`, except `0`.

Any list, tuple, set, and dictionary are `True`, except empty ones.

**Example:**
The following will return True:
```python
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
```
**Output:**
```
True
True
True
```

#### Some Values are False

In fact, there are not many values that evaluate to `False`, except empty values, such as `()`, `[]`, `{}`, `""`, the number `0`, and the value `None`. And of course the value `False` evaluates to `False`.

**Example:**
The following will return False:
```py
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```
**Output:**
```
False
False
False
False
False
False
False
```

One more value, or object in this case, evaluates to `False`, and that is if you have an object that is made from a class with a `__len__` function that returns `0` or `False`:

**Example:**
```python
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
```
**Output:**
```
False
```

#### Functions can Return a Boolean

You can create functions that returns a Boolean Value:

**Example:**
Print the answer of a function:
```python
def myFunction() :
  return True

print(myFunction())
```
**Output:**
```
True
```

You can execute code based on the Boolean answer of a function:

**Example:**
Print `YES!` if the function returns True, otherwise print `NO!`:

```python
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
```
**Output:**
```
YES!
```

Python also has many built-in functions that return a boolean value, like the `isinstance()` function, which can be used to determine if an object is of a certain data type:

**Example:**
Check if an object is an integer or not:
```python
x = 200
print(isinstance(x, int))
```
**Output:**
```
True
```

### String

String in python are surrounded by either single quotation marks or double quotation marks.

`'hello'` is the same as `"hello"`

Assigning a string to a variable is done with the variable name followed by an equal sign and the string

```Python
a = "Hello"

print (a)
```
**Output:**
```
Hello
```

#### Multiline String

You can assign a multiline string to a variable by using three quotes:

```Python
a = """ This is a 
        Multi line 
        String """
```
OR three single quotes:
```Python
a = ''' Name 
        Age
        Number'''
print (a)
```
**Output**:
```
 Name
 Age 
 Number
```

#### Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

**Example:**
```Python
a = "Hello"
print(a)
```
Output:
```
Hello
```

#### Strings are Arrays

Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

**Example:**

Get the character at position 1 (remember that the first character has the position 0):

```py
a = "Hello, World!"
print(a[1])
```
**Output:**
```
e
```

#### Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a `for` loop.

**Example:**
Loop through the letters in the word "banana":

```py
for x in "banana":
  print(x)
```
**Output:**
```
b
a
n
a
n
a
```

#### String Length

To get the length of a string, use the `len()` function.

Example
The `len()` function returns the length of a string:

```python
a = "Hello, World!"
print(len(a))
```
**Output:**
```
13
```
#### Check String

To check if a certain phrase or character is present in a string, we can use the keyword `in`.

**Example:**

Check if `free` is present in the following text:

```py
txt = "The best things in life are free!"
print("free" in txt)
```
**Output:**
```
True
```

Use it in an `if` statement:

**Example:**

Print only if `free` is present:

```python
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```

#### Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.

**Example:**

Check if `expensive` is NOT present in the following text:

```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```
**Output:**
```
True
```

Use it in an `if` statement:

**Example:**

print only if "expensive" is NOT present:

```python
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```
**Output:**
```
No, 'expensive' is NOT present.
```

#### Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

**Example:**

Get the characters from position 2 to position 5 (not included):

```python
b = "Hello, World!"
print(b[2:5])
```
**Output:**
```
llo
```

***`Note`: The first character has index 0.***

#### Slice From the Start

By leaving out the start index, the range will start at the first character:

**Example:**

Get the characters from the start to position 5 (not included):

```python
b = "Hello, World!"
print(b[:5])
```
**Output:**
```
Hello
```

#### Slice To the End

By leaving out the end index, the range will go to the end:

**Example:**

Get the characters from position 2, and all the way to the end:

```python
b = "Hello, World!"
print(b[2:])
```
**Output:**
```
llo World
```

#### Negative Indexing

Use negative indexes to start the slice from the end of the string:

**Example:**

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

```python
b = "Hello, World!"
print(b[-5:-2])
```
**Output:**
```
orl
```

#### Upper Case

**Example:**

The `upper()` method returns the string in upper case:

```python
a = "Hello, World!"
print(a.upper())
```
**Output:**
```
HELLO WORLD!
```

#### Lower Case

**Example:**

The `lower()` method returns the string in lower case:

```python
a = "Hello, World!"
print(a.lower())
```
**Output:**
```
hello world
```

#### Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

**Example:**

The `strip()` method removes any whitespace from the beginning or the end:

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```
**Output:**
```
Hello, World!
```
#### Replace String

**Example:**

The `replace()` method replaces a string with another string:

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```
**Output:**
```
Jello, World
```

#### Split String

The `split()` method returns a list where the text between the specified separator becomes the list items.

**Example:**

The `split()` method splits the string into subs if it finds instances of the separator:

```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```
**Output:**
```
['Hello', ' World!']
```
#### String Concatenation

To concatenate, or combine, two strings you can use the + operator.

**Example:**

Merge variable `a` with variable `b` into variable `c`:

```python
a = "Hello"
b = "World"
c = a + b
print(c)
```
**Output:**
```
HelloWorld
```

**Example:**

To add a space between them, add a `" "`:

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```
**Output:**
```
Hello World
```

#### String Format

As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

**Example:**
```python
age = 36
txt = "My name is John, I am " + age
print(txt)
```
**Output:**
```
TypeError: ...
```

But we can combine strings and numbers by using the `format()` method!

The `format()` method takes the passed arguments, formats them, and places them in the string where the placeholders `{}` are:

**Example:**

Use the `format()` method to insert numbers into strings:

```python
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
```
**Output:**
```
My name is john, and am 36
```

The `format()` method takes unlimited number of arguments, and are placed into the respective placeholders:

**Example:**
```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
```
**Output:**
```
I want 3 pieces of item 567 for 49.95 dollars.
```

You can use index numbers `{0}` to be sure the arguments are placed in the correct placeholders:

**Example:**
```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
```
**Output:**
```
I want to pay 49.95 dollars for 3 pieces of item 567
```

#### Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash `\` followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

**Example:**

You will get an error if you use double quotes inside a string that is surrounded by double quotes:

```python
txt = "We are the so-called "Vikings" from the north."
```
**Output:**
```
SyntaxError: invalid syntax
```

To fix this problem, use the escape character `\"`:


**Example:**
The escape character allows you to use double quotes when you normally would not be allowed:

```python
txt = "We are the so-called \"Vikings\" from the north."
```
**Output:**
```
We are the so-called "Vikings" from the north.
```

#### Escape Characters

Other escape characters used in Python:

| Code |	Result |
| ---- | ------- |
| `\'` | Single Quote	| 
| `\\\\` |	Backslash	 |
| `\n` |	New Line	|
| `\r` |	Carriage Return	| 
| `\t` |	Tab	| 
| `\b` | Backspace	|
| `\f` |	Form Feed	|
| `\ooo` | Octal value	|
| `\xhh` | Hex value |

#### String Methods

Python has a set of built-in methods that you can use on strings.

***`Note`: All string methods return new values. They do not change the original string.***

Checkout: [ String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

### Lists 

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
```Python
list = [ 'value1', value2, 1]
```

#### Indexing items

list first items are indexed at `[0]` index, second `[1]`, etc.

**Example:**
```Python
list1 = ["a", "b", "c"]
print (list1[0])
print (list1[1])
print (list1[2])
```
**Output:**
```
a
b
c
```

#### Negative Indexing

Negative indexing means start from the end

`-1` refers to the last item, `-2` refers to the second last item etc.

**Example:**
Print the last item of the list:
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
**Output:**
```
cheery
```

#### Length

To determine how many items a list has, use the `len()` function:

**Example:**

Print the number of items in the list:
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```
**Output:**
```
3
```

#### Check Datatype

From Python's perspective, lists are defined as objects with the data type 'list':

`<class 'list'>`
**Example:**

What is the data type of a list?
```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
```
**Output:**
```
<class 'list'>
```

#### The list() Constructor

It is also possible to use the `list()` constructor when creating a new list.

**Example:**

Using the `list()` constructor to make a List:
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```
**Output:**
```
['apple', 'banana', 'cherry']
```

#### Slicing 

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

**Example:**
```python
list = ["abc", "def", "ghi", "jkl", "mno"]
print(list[1:3])
```
**Output:**
```
["def", "ghi"]
```


***`Note`: The search will start at index 1 (included) and end at index 3 (not included).***

***Remember that the first item has index 0.***

#### Append Items

To add an item to the end of the list, use the append() method:

**Example:**
Using the `append()` method to append an item:
```python
list = ["apple", "banana", "cherry"]
list.append("orange")
print(list)
```
**Output:**
```
['apple', 'banana', 'cherry', 'orange']
```

#### Insert Items

To insert a list item at a specified index, use the `insert()` method.

The `insert()` method inserts an item at the specified index:

**Example:**
Insert an item as the second position:
```python
list = ["apple", "banana", "cherry"]
list.insert(1, "orange")
print(list)
```
**Output
```
['apple', 'orange', 'banana', 'cherry']
```

***`Note`: As a result of the examples above, the lists will now contain 4 items.***

#### Remove 

The `remove()` method removes the specified item.
**Example:**
```python
list = ['a', 'b', 'c',]
list.remove('b')
print(list)
```
**Output:**
```
['a', 'c']
```

#### Pop 

If you do not specify the index, the `pop()` method removes the last item.

**Example**python
```
list = ["a", "b", "c"]
list.pop()
print(list)
```
**Output:**
```
["a", "b"]
```

#### To delete complete list

The `del` keyword can also delete the list completely.

**Example:**
```python
list = ["a", "b", "c"]
del list
```

#### Clear list

The `clear()` method empties the list.

The list still remains, but it has no content.

**Example:**
```
list = ["a", "b", "c"]
list.clear()
print(list)
```
**Output:**
```
[]
```

#### Adding elements to lists

```python
print(list + ["x", "y", "z"])
```

#### Join lists

**Example:**
```python
list1 = ['a', 'b']
list2 = ['c', 'd']

list3 = list1 + list2
print(list3)
```
**Output:**
```
['a', 'b', 'c', 'd']
```

#### Minimum & Maximum

```Python
list1 = ['a', 'b', 'z']
list2 = ['1', '2', '9']

print(max(list))
print(max(list))

print(min(list))
print(min(list))
```
**Output:**
```
a
z

1
9
```

#### lists methods

Python has a set of built-in methods that you can use on lists.

| Method |	Description |
| ------ | ------------ |
| `append()` | Adds an element at the end of the list |
| `clear()` |	Removes all the elements from the list |
| `copy()` |	Returns a copy of the list |
| `count()`	| Returns the number of elements with the specified value |
| `extend()` |	Add the elements of a list (or any iterable), to the end of the current list |
| `index()` |	Returns the index of the first element with the specified value |
| `insert()` |	Adds an element at the specified position |
| `pop()` | Removes the element at the specified position |
| `remove()` |	Removes the item with the specified value |
| `reverse()` |	Reverses the order of the list |
| `sort()` | Sorts the list |


### Tuples 

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

**Example:**
```Python
tuple1 = ( 1, 2, 3)

print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
```
**Output:**
```
( 1, 2, 3)
1
2
3
```

***'Note': You can't change values, So to update Convert tuple to list by using `list()` function and update as list then convert back to tuple using `tuple()` function.***

***Example:**
```
tuple1 = (1, 2)
list1 = list(tuple1)
# update the list
updated_tuple= tuple(list1)
```

you can use `len()`, `max()`, `min()` function also.
```Python
tuple1 = (1, 2, 3, 4)

print(len(tuple1)) # length 4
print(max(tuple1)) # maximum value = 4
print(min(tuple1)) # minimum value = 1
```


### Dictionary 

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

**Example:**
```Python
dict_name = {
  "key1" : "value1",
  "key2" : 1,
}

print(dict_name('key1')) # prints value1
print(dict_name.keys()) # prints all keys
print(dict_name.values()) # prints all values
```
**Output:**
```
value1
{ "key1", "key2" }
{ 'value1', 1}
```


Dictionaries cannot have two items with the same key:

#### Adding Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

**Example:**
```
dict = { "key1" : "value1", "key2" : "value2", }
dict["key3"] = "value3"
print(dict)
```
**Output:**
```
{ "key1" : "value1", "key2" : "value2", "key3" : "value3",}
```

#### Updating 

The `update()` method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

**Example:**
```Python
dict_name.update({'key1' : 'val'})
print(dict_name[key1])
```
**Output:**
```
val
```

#### Removing Items

There are several methods to remove items from a dictionary:

The `pop()` method removes the item with the specified key name:
**Example:**
```
dict.pop("key")
```

The del keyword removes the item with the specified key name:
**Example:**
```
del dict["key"]
```

The `del` keyword can also delete the dictionary completely:
**Example:**
```
del dict
```

The `clear()` method empties the dictionary:
**Example:**
```
dict.clear()
```

#### Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

| Method | Description |
| ------ | ----------- |
| `clear()` |	Removes all the elements from the dictionary |
| `copy()` | Returns a copy of the dictionary |
| `fromkeys()` |	Returns a dictionary with the specified keys and value |
| `get()`	| Returns the value of the specified key |
| `items()` |	Returns a list containing a tuple for each key value pair |
| `keys()` |	Returns a list containing the dictionary's keys |
| `pop()` |	Removes the element with the specified key
| `popitem()`	| Removes the last inserted key-value pair
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| `update()` |	Updates the dictionary with the specified key-value pairs |
| `values()` |	Returns a list of all the values in the dictionary |

### Sets 

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable, ,unindexed and not allow duplicate values.

***`Note`: Set items are unchangeable, but you can remove items and add new items.***

Sets are written with curly brackets.

**Example:**
```Python
set = { 'value1', 'value2' }
```

***`Note`: Sets are unordered, so you cannot be sure in which order the items will appear***

#### length, type & set() constructor

```Python
set = { 'a', 'b', 'c', 'd', 'e' }
print(len(dict)

print(type(dict))

tuple = ("a", "b")
set = set(tuple)
print(set)
```
**Output:**
```
5

<class 'set'>

{ 'a',  'b' }
```

#### Access Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

**Example:**
Loop through the set, and print the values:
```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```
**Output:**
```
banana
apple
cherry 
```

**Example:**
Check if "banana" is present in the set:
```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```
**Output:**
```
True
```

#### Add Items

To add one item to a set use the add() method.

**Example:**
Add an item to a set, using the `add()` method:
```python
set = {"apple", "banana", "cherry"}

set.add("orange")

print(set)
```
**Output:**
```
{'orange', 'banana', 'apple', 'cherry'}
```

#### Add Sets

To add items from another set into the current set, use the `update()` method.

**Example:**
Add elements from ``tropical` into `thisset`:
```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```
**Output:**
```
{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
```

#### Add Any Iterable

The object in the `update()` method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

**Example:**
Add elements of a list to at set:
```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
```
**Output:**
```
{'banana', 'cherry', 'apple', 'orange', 'kiwi'}
```

#### Remove Item

To remove an item in a set, use the `remove()`, or the `discard()` method.

**Example:**
```
set = { 'a', 'b', 'c'}

set.remove('b')
```

***`Note`: If the item to remove does not exist, remove() will raise an error.***

**Example:**
```
set.discard('b')
```

***`Note`: If the item to remove does not exist, `discard()` will NOT raise an error.***


You can also use the `pop()` method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the `pop()` method is the removed item.

**Example:**
```
set.pop()
```

***`Note`: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.***

The `clear()`  Method empties the set:
```
set.clear()
```

The `del` keyword will delete the set completely:
```
del set
```

#### Set Methods

Python has a set of built-in methods that you can use on sets.

| Method | Description |
| ------ | ----------- |
| `add()` |	Adds an element to the set |
| `clear()`	| Removes all the elements from the set |
| `copy()` |	Returns a copy of the set |
`difference()` |	Returns a set containing the difference between two or more sets |
`difference_update()`	| Removes the items in this set that are also included in another, specified set
`discard()`	Remove the specified item |
| `intersection()` |	Returns a set, that is the intersection of two other sets |
`intersection_update()` |	Removes the items in this set that are not present in other, specified set(s) |
| `isdisjoint()` | Returns whether two sets have a intersection or not |
| `issubset()` | Returns whether another set contains this set or not |
| `issuperset()` | Returns whether this set contains another set or not |
| `pop() | Removes an element from the set |
| `remove()` | Removes the specified element |
| `symmetric_difference()` | Returns a set with the symmetric differences of two sets |
| `symmetric_difference_update()`	| inserts the symmetric differences from this set and another |
| `union()` |	Return a set containing the union of sets |
| `update()` |	Update the set with the union of this set and others |

### Arrays

Arrays are used to store multiple values in one single variable

**Example:**
Create an array containing car names:
```python
cars = ["Ford", "Volvo", "BMW"]
```
**Output:**
```
["Ford", "Volvo", "BMW"]
```
#### What is an Array?

An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"


However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.

#### Access the Elements of an Array

You refer to an array element by referring to the index number.

**Example:**
Get the value of the first array item:
```python
x = cars[0]
```
**Output:**
```
Ford
```

**Example:**
Modify the value of the first array item:
```python
cars[0] = "Toyota"
```
**Output:**
```
['Toyota', 'Volvo', 'BMW']
```

#### Length

Use the `len()` method to return the length of an array (the number of elements in an array).

**Example:**
Return the number of elements in the `cars` array:
```python
x = len(cars)
```
**Output:**
```
3
```

***`Note`: The length of an array is always one more than the highest array index.***

#### Looping Array Elements

You can use the `for in` loop to loop through all the elements of an array.

**Example:**
Print each item in the `cars` array:
```python
for x in cars:
  print(x)
```
**Output:**
```
Ford
Volvo
BMW
```

#### Adding Array Elements

You can use the `append()` method to add an element to an array.

**Example:**
Add one more element to the `cars` array:
```python
cars.append("Honda")
```
**Output:**
```
['Ford', 'Volvo', 'BMW', 'Honda']
```

#### Removing Array Elements

You can use the `pop()` method to remove an element from the array.

**Example:**
Delete the second element of the cars array:
```python
cars.pop(1)
```
**Output:**
```
['Ford', 'BMW']
```

You can also use the `remove()` method to remove an element from the array.

**Example:**
Delete the element that has the value `Volvo`:
```python
cars.remove("Volvo")
```
**Output:**
```
['Ford', 'BMW']
```

***`Note`: The list's `remove()` method only removes the first occurrence of the specified value.***

#### Array Methods

Python has a set of built-in methods that you can use on lists/arrays.

| Method |	Description |
| ------ | ------------ |
| `append()` | Adds an element at the end of the list |
| `clear()`	| Removes all the elements from the list |
| `copy()` |	Returns a copy of the list |
| `count()`	| Returns the number of elements with the specified value |
| `extend()` | Add the elements of a list (or any iterable), to the end of the current list |
| `index()`	| Returns the index of the first element with the specified value |
| `insert()` | Adds an element at the specified position |
| `pop()` | Removes the element at the specified position |
| `remove()` | Removes the first item with the specified value |
| `reverse()` | Reverses the order of the list |
| `sort()` | Sorts the list |


### Functions

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

**Types of functions**

- Built-in functions
- User-defined functions

#### Defining a functions

- Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).

- Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

- The first statement of a function can be an optional statement - the documentation string of the function or docstring.

- The code block within every function starts with a colon (:) and is indented.

- The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

**Syntax** :
```Python
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
```

**Example** :
```Python
def printme( str ):
   "This prints a passed string into this function"
   print str
   return
```

#### Calling a function

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

```Python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")
```

**Output** :
```Python
I'm first call to user defined function!
Again second call to the same function
```

#### Pass by reference vs values

All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. 

**Example** :
```Python
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
```

**Output** :
```
Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]
```

#### Function arguments

- Required arguments
- Keyword arguments
- Default arguments
- Variable-length arguments

##### Required arguments

Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.

To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows

```Python
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme() # empty argument throwing an error
```

**Output** :
```
Traceback (most recent call last):
   File "test.py", line 11, in <module>
      printme();
TypeError: printme() takes exactly 1 argument (0 given)
```

##### Keywords arguments

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.

This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the printme() function in the following ways

**Example** :
```Python
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme( str = "My string")
```

**Output**: 
```Python
My string
```

The following example gives more clear picture. Note that the order of parameters does not matter.

**Example** :
```Python
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age: ", age
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
```

**Output** :
```
Name:  miki
Age:  50
```

##### Default arguments 

A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

**Example** :
```Python
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age: ", age
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )
```

**Output** :
```
Name:  miki
Age:  50
Name:  miki
Age:  35
```

##### Variable-length arguments

You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

**Syntax** :
```Python
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
```

An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example

**Example** :
```Python
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
```
**Output** :
```
Output is:
10
Output is:
70
60
50
```

##### ***Anonymous*** function 

These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.

- Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

- An anonymous function cannot be a direct call to print because lambda requires an expression

- Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

- Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function stack allocation during invocation for performance reasons.

**Syntax** :
```Python
lambda [arg1 [,arg2,.....argn]]:expression
```

**Example** :
```Python
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )
```
**Output** :
```
Value of total :  30
Value of total :  40
```

#### The Return statement

The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

**Example** :
```Python
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "Inside the function : ", total
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total 
```

**Output** :
```
Inside the function :  30
Outside the function :  30
```

#### Variables Scope

All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.

The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python −

- Global variables
- Local variables

Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.

This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope. Following is a simple example.

**Example** :
```Python
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;

# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 
```
**Output** :
```
Inside the function local total :  30
Outside the function global total :  0
```

### Classes / Objects

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

#### Create a Class

To create a class, use the keyword `class`:

**Example:**
Create a class named MyClass, with a property named x:
```python
class MyClass:
  x = 5
```
**Output:**
```
<class '__main__.MyClass'>
```

#### Create Object

Now we can use the class named MyClass to create objects:

**Example:**
Create an object named p1, and print the value of x:
```python
p1 = MyClass()
print(p1.x)
```
**Output:**
```
5
```

#### The __init__() Function

The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

**Example:**
Create a class named Person, use the __init__() function to assign values for name and age:
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```
**Output:**
```
John
36
```

***`Note`: The __init__() function is called automatically every time the class is being used to create a new object.***

#### Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

**Example:**

Insert a function that prints a greeting, and execute it on the p1 object:
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```
**Output:**
```
Hello my name is John
```

***`Note`: The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.***

#### The self Parameter

The `self` parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named `self` , you can call it whatever you like, but it has to be the first parameter of any function in the class:

**Example:**
Use the words mysillyobject and abc instead of self:
```python
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```
**Output:**
```
Hello my name is John
```

#### Modify Object Properties

You can modify properties on objects like this:

**Example:**
Set the age of p1 to 40:
```python
p1.age = 40
```
**Output:**
```
40
```

#### Delete Object Properties

You can delete properties on objects by using the `del` keyword:

**Example:**
Delete the age property from the p1 object:
```python
del p1.age
```
**Output:**
```
AttributeError: 'Person' object has no attribute 'age'
```

#### Delete Objects

You can delete objects by using the `del` keyword:

**Example:**
Delete the p1 object:
```python
del p1
```
**Output:**
```
NameError: 'p1' is not defined
```

#### The pass Statement

`class` definitions cannot be empty, but if you for some reason have a `class` definition with no content, put in the `pass` statement to avoid getting an error.

**Example:**
```python
class Person:
  pass
```

### Modules

**What is a Module?**

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

#### Create a Module

To create a module just save the code you want in a file with the file extension `.py`:

**Example**:

Save this code in a file named `mymodule.py`

```py
def greeting(name):
  print("Hello, " + name)
```

#### Use a Module

Now we can use the module we just created, by using the `import` statement:

**Example**:

Import the module named mymodule, and call the greeting function:

```py
import mymodule

mymodule.greeting("Jonathan")
```
**Output** :
```
Hello, Jonathan
```
**`Note`: When using a function from a module, use the syntax: module_name.function_name.**

##### Variables in Module

The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

**Example** :

Save this code in the file `mymodule.py`
```py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

**Example**:

Import the module named mymodule, and access the person1 dictionary:
```py
import mymodule

a = mymodule.person1["age"]
print(a)
```
**Output** :
```
36
```

#### Naming a Module

You can name the module file whatever you like, but it must have the file extension `.py`

#### Re-naming a Module

You can create an alias when you import a module, by using the `as` keyword:

**Example**:

Create an alias for `mymodule` called `mx`:
```py
import mymodule as mx

a = mx.person1["age"]
print(a)
```
**Output** :
```py
36
```

#### Built-in Modules

There are several built-in modules in Python, which you can import whenever you like.

**Example**:

Import and use the `platform` module:
```py
import platform

x = platform.system()
print(x)
```
**Output** :
```
Windows 
```

#### Using the dir() Function

There is a built-in function to list all the function names (or variable names) in a module. The `dir()` function:

**Example**:

List all the defined names belonging to the platform module:
```py
import platform

x = dir(platform)
print(x)
```
**Output** :
```
['DEV_NULL', '_UNIXCONFDIR',...
```
**`Note`: The dir() function can be used on all modules, also the ones you create yourself.**

#### Import From Module

You can choose to import only parts from a module, by using the `from` keyword.

**Example**

The module named `mymodule` has one function and one dictionary:
```py
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```
**Example**

Import only the person1 dictionary from the module:
```py
from mymodule import person1

print (person1["age"])
```
**Output** :
```
36
```

**`Note`: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not ~~mymodule.person1["age"]~~`**

### Try Except Else Finally

The `try` block lets you test a block of code for errors.

The `except` block lets you handle the error.

The `else` block lets you execute code when there is no error.

The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

#### Exception Handling

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the `try` statement:

**Example:**
The `try` block will generate an exception, because x is not defined:
```python
try:
  print(x)
except:
  print("An exception occurred")
```
**Output:**
```
An exception occurred
```

Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:

**Example:**
This statement will raise an error, because `x` is not defined:
```python
print(x)
```
**Output:**
```
NameError: name 'x' is not defined
```

#### Many Exceptions

You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

**Example:**
Print one message if the try block raises a `NameError` and another for other errors:
```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
**Output:**
```
Variable x is not defined
```

#### Else

You can use the `else` keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the `try` block does not generate any error:
```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```
**Output:**
```
Hello
Nothing went wrong
```

#### Finally

The `finally` block, if specified, will be executed regardless if the try block raises an error or not.

**Example:**
```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```
**Output:**
```
Something went wrong
The 'try except' is finished
```

This can be useful to close objects and clean up resources:

**Example:**
Try to open and write to a file that is not writable:
```python
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```
**Output:**
```
Something went wrong when writing to the file
```

The program can continue, without leaving the file object open.

#### Raise an exception

As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the `raise` keyword.

**Example:**
Raise an error and stop the program if x is lower than 0:
```python
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```
**Output:**
```
Exception: Sorry, no numbers below zero
```

The `raise` keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

**Example:**
Raise a TypeError if x is not an integer:
```python
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
```
**Output:**
```
TypeError: Only integers are allowed
```

#### Exceptions & Description 

| Exception Name | Description |
| -------------- | ----------- |
| Exception | Base class for all exceptions |
| StopIteration | Raised when the next() method of an iterator does not point to any object. |
| SystemExit | Raised by the sys.exit() function. |
| StandardError | Base class for all built-in exceptions except StopIteration and SystemExit. |
| ArithmeticError | Base class for all errors that occur for numeric calculation. |
| OverflowError | Raised when a calculation exceeds maximum limit for a numeric type. |
| FloatingPointError | Raised when a floating point calculation fails. |
| ZeroDivisionError | Raised when division or modulo by zero takes place for all numeric types. |
| AssertionError | Raised in case of failure of the Assert statement. |
| AttributeError | Raised in case of failure of attribute reference or assignment. |
| EOFError | Raised when there is no input from either the raw_input() or input() function and the end of file is reached. |
| ImportError | Raised when an import statement fails. |
| KeyboardInterrupt | Raised when the user interrupts program execution, usually by pressing Ctrl+c. |
| LookupError | Base class for all lookup errors. |
| IndexError | Raised when an index is not found in a sequence. |
| KeyError | Raised when the specified key is not found in the dictionary. |
| NameError | Raised when an identifier is not found in the local or global namespace. |
| UnboundLocalError | Raised when trying to access a local variable in a function or method but no value has been assigned to it. |
| EnvironmentError | Base class for all exceptions that occur outside the Python environment. |
| IOError | Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist. |
| IOError | Raised for operating system-related errors.|
| SyntaxError | Raised when there is an error in Python syntax. |
| IndentationError | Raised when indentation is not specified properly. |
| SystemError | Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit. |
| SystemExit | Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit. |
| TypeError | Raised when an operation or function is attempted that is invalid for the specified data type. |
| ValueError | Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified. |
| RuntimeError | Raised when a generated error does not fall into any category. |
| NotImplementedError | Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented. |

-------------------------------------------------------

## Advanced Python

### PIP

#### What is PIP?

PIP is a package manager for Python packages, or modules if you like.

***`Note`: If you have Python version 3.4 or later, PIP is included by default.***

#### What is a Package?

A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

#### Check if PIP is Installed

Navigate your command line to the location of Python's script directory, and type the following:

**Example:**
Check PIP version:
```shell
pip --version
```

#### Install PIP

If you do not have PIP installed, you can download and install it from this page: [pypi.org](https://pypi.org/project/pip/)

#### Download a Package

Downloading a package is very easy.

Open the command line interface and tell PIP to download the package you want.

Navigate your command line to the location of Python's script directory, and type the following:

Example
Download a package named "camelcase":
```shell
pip install camelcase
```

#### Using a Package

Once the package is installed, it is ready to use.

Import the "camelcase" package into your project.

**Example:**
Import and use "camelcase":
```python
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```
**Output:**
```
Lorem Ipsum Dolor Sit Amet
```

#### Find Packages

Find more packages at [pypi](https://pypi.org/).

#### Remove a Package

Use the `uninstall` command to remove a package:

**Example:**
Uninstall the package named "camelcase":
```shell
pip uninstall camelcase
```

#### List Packages

Use the `list` command to list all the packages installed on your system:

**Example:**
List installed packages:
```
pip list
```

### JSON

JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

#### JSON in Python

Python has a built-in package called `json`, which can be used to work with JSON data.

**Example:**
Import the json module:
```python
import json
```


#### Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the `json.loads()` method.

The result will be a Python dictionary.

**Example:**
Convert from JSON to Python:
```python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```
**Output:**
```
30
```

#### Convert from Python to JSON

If you have a Python object, you can convert it into a JSON string by using the `json.dumps()` method.

**Example:**
Convert from Python to JSON:
```python
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```
**Output:**
```
{"name": "John", "age": 30, "city": "New York"}
```

You can convert Python objects of the following types, into JSON strings:

- dict
- list
- tuple
- string
- int
- float
- True
- False
- None

**Example:**
Convert Python objects into JSON strings, and print the values:
```python
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
```
**Output:**
```
{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null
```

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

| Python | JSON |
| ------ | ---- |
| dict | Object |
| list	| Array |
| tuple	| Array |
| str	| String |
| int | Number |
| float | Number |
| True |	true |
| False |	false |
| None |	null |

**Example:**
Convert a Python object containing all the legal data types:
```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
```
**Output:**
```
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
```

#### Format the Result

The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The `json.dumps()` method has parameters to make it easier to read the result:

**Example:**
Use the `indent` parameter to define the numbers of indents:
```python
json.dumps(x, indent=4)
```
**Output:**
```
{
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
```

You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

Example
Use the `separators` parameter to change the default separator:
```python
json.dumps(x, indent=4, separators=(". ", " = "))
```
**Output:**
```
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
```

#### Order the Result

The `json.dumps()` method has parameters to order the keys in the result:

Example
Use the `sort_keys` parameter to specify if the result should be sorted or not:
```python
json.dumps(x, indent=4, sort_keys=True)
```
**Output:**
```
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}
```


### File handling

File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

#### Basics

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

`r` - Read - Default value. Opens a file for reading, error if the file does not exist

`a` - Append - Opens a file for appending, creates the file if it does not exist

`w` - Write - Opens a file for writing, creates the file if it does not exist

`x` - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

`t` - Text - Default value. Text mode

`b` - Binary - Binary mode (e.g. images)

**Syntax**:

To open a file for reading it is enough to specify the name of the file:

```py
f = open("demofile.txt")
```
The code above is the same as:

```py
f = open("demofile.txt", "rt")
```

Because `r` for read, and `t` for text are the default values, you do not need to specify them.

***`Note`: Make sure the file exists, or else you will get an error.***

#### Modes & Description

| Modes | Description |
| ----- | ----------- |
| `r` | Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode. |
| `rb` | Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode. |
| `r+` | Opens a file for both reading and writing. The file pointer placed at the beginning of the file. |
| `rb+` | Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file. |
| `w` | Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. |
| `wb` | Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. |
| `w+` | Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing. |
| `wb+` | Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing. |
| `a` | Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing. |
| `ab` | Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing. |
| `a+` | Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. |
| `ab+` | Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. |

####  Open a File

To open the file, use the built-in open() function.

The `open()` function returns a file object, which has a `read()`` method for reading the content of the file:

**Example:**
```py
f = open("file.txt", "r")
print(f.read())
```
**Output:**
```
Hello! Welcome to file.txt
This file is for testing purposes.
Good Luck!
```

If the file is located in a different location, you will have to specify the file path, like this:

**Example:**
Open a file on a different location:
```py
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
```
**Output:**
```
Welcome to this text file!
This file is located in a folder named "myfiles", on the D drive.
Good Luck!
```

#### Read Only Parts of the File

By default the `read()` method returns the whole text, but you can also specify how many characters you want to return:

**Example:**

Return the 5 first characters of the file:

```py
f = open("demofile.txt", "r")
print(f.read(5))
```
**Output:**
```
Hello
```


#### Read Lines

You can return one line by using the `readline()` method:

**Example:**

Read one line of the file:
```py
f = open("demofile.txt", "r")
print(f.readline())
```
**Output:**
```
Hello! Welcome to file.txt
```

By calling `readline()`` two times, you can read the two first lines:

**Example:**

Read two lines of the file:
```py
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
```
**Output:**
```
Hello! Welcome to file.txt
This file is for testing purposes.
```

By looping through the lines of the file, you can read the whole file, line by line:

**Example:**

Loop through the file line by line:
```py
f = open("demofile.txt", "r")
for x in f:
  print(x)
```
**Output:**
```
Hello! Welcome to file.txt
This file is for testing purposes.
Good Luck!
```

#### Close Files

It is a good practice to always close the file when you are done with it.

**Example:**

Close the file when you are finish with it:
```py
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```

***`Note`: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.***


#### Write to an Existing File

To write to an existing file, you must add a parameter to the `open()`` function:

`a` - Append - will append to the end of the file

`w` - Write - will overwrite any existing content

**Example:**

Open the file `demofile2.txt` and append content to the file:
```py
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```
**Output**:
```
Hello! Welcome to demofile2.txt
This file is for testing purposes.
Good Luck!Now the file has more content!
```

**Example:**

Open the file `demofile3.txt` and overwrite the content:
```py
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
```
**Output**:
```
Woops! I have deleted the content!
```

***`Note`: the `w` method will overwrite the entire file.***

#### Create a New File

To create a new file in Python, use the `open()`` method, with one of the following parameters:

`x` - Create - will create a file, returns an error if the file exist

`a` - Append - will create a file if the specified file does not exist

`w` - Write - will create a file if the specified file does not exist

**Example:**
Create a file called `myfile.txt`:
```py
f = open("myfile.txt", "x")
```

Result: a new empty file is created!

**Example:**
Create a new file if it does not exist:
```py
f = open("myfile.txt", "w")
```

#### Delete a File

To delete a file, you must import the OS module, and run its `os.remove()`` function:

**Example:**

Remove the file `demofile.txt`:
```py
import os
os.remove("demofile.txt")
```
#### Check if File exist

To avoid getting an error, you might want to check if the file exists before you try to delete it:

**Example:**

Check if file exists, then delete it:
```py
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

#### Create a folder

The `os` module has serveral methods that helps you create, remove, and change directories.

```py
os.mkdir("newdir")
```

#### Delete Folder

To delete an entire folder, use the `os.rmdir()` method:

**Example:**

Remove the folder `myfolder`:
```py
import os
os.rmdir("myfolder")
```
***`Note`: You can only remove empty folders.***

#### Change a directory

**Syntax**:
```py
import os
# os.chdir("path")
os.chdir("/home")
```

Check more methods

***Reference:***

[File Methods](https://www.tutorialspoint.com/python/file_methods.htm)

[OS Module Methods](https://www.tutorialspoint.com/python/os_file_methods.htm)
