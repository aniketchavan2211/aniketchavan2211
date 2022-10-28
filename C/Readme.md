## C Language

### Introduction to C 

C was invented in **1972**. It's one of the oldest language to ne used
even today.
It is one of the most widely used programming language in the world.
It has influenced many popular language, especially **C++ ( Cpp )**.

**Simple:** - C is a Structure based language i.e. we can divide a big program into multiple parts, which makes it easy to write and understand.

**Efficient and Fast:** 
- C is considered to be "close to the computer," meaning we can program the computer to do precisely what we want. 
**Portable:** -  Program written in C can be run on different types of machines with little or no modification.

**Used for: **
- For creating desktop applications.
- For developing games.
- For designing Operating System. 
- For designing Compilers. 

**Working of C**
1. **Writing Souce code:** The first step to write a source code for the desired project. The code is written using a Text Editor.

2. **Compiling the source code:** The Source code is then converted into equivalent machine instructions, so that the computer can understand it.

3. **Checking for Errors:** The code is checked for all possible errors.

4. **Linking:** The code is linked with other files code
At the beginning of the code header files means other files are mentioned to link the other code with this script. 

5. **Checking for Errors:** The code is checked for all possible errors once again. 

6. **Execution:** The code is then finally executed to get the desired output. 

### Hello World 

To display output on screen used `printf()` built-in  Function. 

we need to create main function 
```c 
#include <stdio.h> 

int main() {
  printf("Hello World\n");
  // Code to execute 
  return 0;
}
```

`#include <stdio.h>` is header file for input/output files in C, everytime you need to input and output you need to mention the header file at beginning of script.

`int` stand for integer a datatype for numbers(0 - 9).

`main()` main function main is name of function and in 
`()` we pass parameters(remain blank `()` will also work).

`{}` in curly braces contain code to be executed.

`printf("Hello World")` prinf() is function and Hello World is a string because enclosed in double quotation.
**Always Use Double Quotes**

`\n` use for new line 

`;` end of the statement

`/ Comment /` used for Single - Line Comments 

```
/* Beginning of Multi-line Comment

End of Multi-line Comment*/
```

`return 0;` return is keyword at end of the function to take the value out of function, make sure `returntype` and `return value` are same. `0` is and integer(int).
`returntype` is at start of the function before name of functions ` int main()` 

`}` is end of the function 

**Output:**
```c 
Hello World
```
**Running on Linux**
1. First install package clang
```
apt-get install clang
```

2. compile c file
```
clang file.c
```

3. Execute c file
```
./a.out
```

### Syntax 

```c
#include <header file>

returntype functionName(parameters) {
  return 0;
}
```

```C
#include <stdio.h>

int main() {
  return 0;
}
```  

###  Comments

Comments help programmers to understand the program code does.
Comments are short summary or description about code.

Comments are lgnored by Compiler, Comments are not compiled, write a comment to understand the code how it's code execute. 


#### Single-line Comments 

`// Comments `you can one line comment, the line will be ignored by compiler, you can also comment the code.

but what if you want to comment more than 15 lines.
You can add `//` at beginning of line not all.

```C
// Comments are here 
```

#### Mutli-line Comments

```C 
/* Begining of 
Multi-line Comments

End of
Multi-line Comments */
```

Use for multi-line.

### Input / Output

prinf() is use for ouput.
```
printf("Hi");
```

Display `Hi` on screen.

scanf() is use for input.
```
scanf("%d", &var);
```
take input as number and store in `var` variable name.

### Variables and Values

What if you want store something. 
Variables are like containers or boxes stored values like numbers, string, decimals numbers, etc.


```C
// Variable Initialization 

int main() { 
  int variable_name = value;
return 0;
}
``` 
Define dataype, variable_name and value in line.

**Example**
```C 
// Variable Defination 

int main() { 
  int a;
  a = 2;
  return 0;
}
```

### Datatypes 

Values are of many types:

- int
integers, numbers 0 to 9 are intergers datatype.

- char
character, 'A' - 'Z' 'a - b' single letter, character enclosed with `single quotation`.

- float 
floating-point number/decimal number with 7 decimal places 0.123

- double
decimal number with 15 decimal places 0.123456789012345 

#### print Variables

```
int varname = 23;
printf("%d", varname);
```

first initialise variable then use printf function 
adding `"%d"` as digit as datatype. specifying the variable.

``` 
char varname = 'A';
printf("use as %c", varname);
```

**Output:**
```C
use as A
```
`use as` is a string enclosed in double quotation and `%c` specify the variable use here is `%c` for character  

### Decision Making 

Computer can take decision on based of input or according to result. 

`True` or `False`, `Yes` or `No` are examples of decisions.

#### Conditional Statements

- if 
- else 

**Syntax:**
```C 
if (condition) {
  printf("condition is TRUE");
}else {
  printf("condition is FALSE")
}
```

if block execute when condition is True or else block will execute.

**Example:**
```c
int a = 0;
if (a > 2) {
  printf("a is greater than 2");
}else {
  printf("a is less than 2");
}
```

**Output:**
```
a is less than 2
```

### Loops 

What if you need to repeat the task/function/... 

We use Loops for it.

#### Types of Loops 
- for loops
- while loops
- do... while Loops

##### For loops

**Syntax:**
```c
for (init; condition;  increment/decrement) {
  // Your Task to execute 
}
```

1. for loops start with **for** keyword. 
2. **init** This is starting value that will checked and increment in the condition.
3. **condition** loops repeating itself until the condition is false.
4. **increment** varaible keep increase until the condition is true.
5. write code inside in `{}` curly braces.
6. init, condition and increment are separated by `;` semicolon.

**Example:**
```c 
for (i = 1; i < 6; i++){
  // Rest of code
  printf("Hello");
}
```

1. **init** (i = 1) variable `i` initial as `1`. loops start from `1` and end `5`.
2. **condition** (i < 6) loop will repeat till 5 times at 6 time condition is false so loop ends. 
3. **increament** (i++) value will increase 1 time each loop execute. 

**Output:**
```
Hello
Hello
Hello
Hello
Hello
```
##### While loops

**Syntax:**
```C 
// first initialazed the variable
while (condition) {
  // Code to be Execute
}
```

**Example:**
```
int a = 1;
while (a < 6) {
  // Code to be executed
  printf("Hi");
  a++
}
```

1. firstly initialazed Variable a = 1. loop start from 1 till 5.
2. `while` keyword for while loop.
3. condition i < 6 means loops will start from 1 and end 5, loops execute 5 times. if a = 0 than loops will run 6 times.
4. write taks in `{}`` curly braces.
5. at last before close curly brace increament variable
`a++`.

**Output:**
```
Hi // i = 1
Hi // i = 2
Hi // i = 3
Hi // i = 4
Hi // i = 5
```

##### Do... While loops 

**Syntax:**
```C 
int a = 0; // Initialisation
do {
  // Code 
} while (condition);
```

**Example:**
```C 
int i = 1;
do {
  printf();
  i = i + 1;
} while (i < 1);
```

This loop will execute at least one time. condition is false then also loop run 1 time. condition check at last.

####

### Arrays 

Array is variable that contains multiple values but same datatype (numbers/string, etc) and identify by index number. index number start from 0. Arrays value called elements.

Numbers of elements in Arrays can store is called arrays
size 

**Arrays Declaration**

```
datatype arrayname [arraysize];
```

```
int array[5];
```

**Arrays Initialization**

means giving value to an arrays or assigning value to an array.

```
array[0] = 5;
array[1] = 6;
array[2] = 7;
array[3] = 8;
array[4] = 8;
array[5] = 9;
```
 
 **One line**
```
int array[5] = {5, 6, 7, 8, 9};
```

#### Accessing Array

Accessing array by for loop through index.

```C 
int array[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 5; i++) {
  printf("Value at the element %d is %d\n", i, array[i]);
}
```

**Output**
```
Value at the element 0 is: 1 
Value at the element 1 is: 2
Value at the element 2 is: 3
Value at the element 3 is: 4
Value at the element 4 is: 5
``` 

### Function 

Function is group of statements.

**Syntax:**
```C 
returntype functionName (parameters) {
  // Function Body
  return value;
}
```

`returntype` : if you want your function to return some values as a result of the task, the datatype of this return value will com here. 

`void`: If your function doesn't return any value, then `void` is use.

`functionName`: give function a name. 

`(parameters)`: You can pass values to function to perform task. parameters are separated by `,` comma
parameters are optional.

`function body` write task here enclosed with `{}` curly braces.

`return value;`: if you want to return any value you have write `return value;` at end of function body before enclosed of `}` closing curly brace.
Make sure to datatype of `returntype` and `return value` are same


```C
int addition (int num1,int num2) {
  int result;
  result = num1 + num2;
  return result;
}
```

to call a function, addition function.
```
int a = 10;
int b = 20;
int c;

c = addition(a,b);
printf("Addition is %d",c);
```