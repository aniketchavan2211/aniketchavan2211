## Cpp (C++)

### Introduction 

C++ (pronounced "C plus plus") is a high-level general-purpose programming language created by Danish computer scientist `Bjarne Stroustrup` as an extension of the C programming language, or `"C with Classes"`. The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features in addition to facilities for low-level memory manipulation. It is almost always implemented as a compiled language, and many vendors provide C++ compilers, including the Free Software Foundation, LLVM, Microsoft, Intel, Embarcadero, Oracle, and IBM, so it is available on many platforms.

Cpp is very close to hardware. 
-  Java Virtual Machine
-  ATM machine

### Comments

Comments are ignored by C compiler, Programmer use to write description of code.
we comment code that should not execute but remain in code.

#### Single-line Comments

`//` is used for single line comment

```cpp
#include <iostream>
using namespace std;

int main() {
  cout << "Hello" << endl; // World
  return 0;
}

// Hello World
```

here World and Hello World is ignored by compiler,
it not throw an error or print on screen.


#### Multi-line Comments

What if we want to comment more than 15 line of code.
At begining of Multi-line Comments `/*`
and at end `*/`

**Syntax:**
```cpp
int main() {
  /*  Multi-line
  Comments */
  return 0;
}
```

here. Multi-line comment is ignored.
two line of code are ignored.

### Hello World

```cpp
#include <iostream>
using namespace std;

int main(){
  cout << "Hello, World!";
  return 0;
}
```

### Variables and DataTypes

Variables are like containers or storage, use to store values - strings, integers, double, booleans, etc

```cpp
string variable_name = "Value";
```
let's print on screen,
```
cout << variable_name;
// Output: Value
```

#### DataTypes

- integers (int) : to store numbers.

- floating-point numbers (float) : to store fractional/decimal numbers.

- double : to store decimal numbers larger than float.

- character (char) : to store single character or letter.

- string : to store a words/sequenceof characters.

- Booleans (bool) : to store booleans true and false.

#### Scope 

- local scope
variables are defined in functions are called local variables. local variables are used only in that function.

- global scope
variables are defined outside of functions in programs.
global variables are access in whole script.
but local variables are not. can access any function.

### User Input

`cin` used for taking input from user and store in variable, `cout` used for output/print.

`<<` : insertion operator 
`>>` : extraction operator

```cpp
cin >> name; 
// keyboard
cout << 'Name: ' << name;
```

### Decision Making

```cpp
if (condition) {
  // condition is true
} else {
  // condition is false
}
```

```cpp
switch (condition/variable) {
  case 'value1':
    // statement
    break;
  case 'value2':
    // statement
    break;
  case 'value3':
    // statement
    break;
  default:
    // statement
}
```

### Loops

#### for Loops

```cpp
for (init.. ; condition; increment) {
  // statements
}
```

#### while Loop

```cpp
while (condition) {
  // statements  
}
```

#### do.. while loop

```cpp
do {
  // statements
} while (condition);
```

### Arrays

Variable store multiple same datatypes values.

```cpp
datatype arrayName[arraySize];

int roll_no[5]; 

datatype arrayName[index] = value;
int roll_no[0] = 1;
int roll_no[1] = 2;
int roll_no[2] = 3;
int roll_no[3] = 4;
int roll_no[4] = 5;

int roll_no[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 5; i++) {
  cout << i << roll_no[i] // index elements/values
}
```

### Functions

**Syntax:**
```cpp
returnType functionName(parameter1, parameter2) {
  // body of the function
}
```