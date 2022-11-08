## Java

### Hello World
```java

public Hello
{
  public static void main(String[] args)
  {
    System.out.println("Hello, World \n ");
  }
}
```

To Compile to `.class`
```bash
ecj Hello.java
```

Then to .class convert to `dexfile.dex`
```bash
dx --dex --output=hello.dex Hello.class
```

Run in Dalvikvm 
```bash
dalvikvm -cp hello.dex Hello
```

### Comment

Comments are very usefull for developer or other programmer.
Comments are ignored by Java Interpreter, so programmer describle the code.


```java
// Comments 
```

### Input / Output

**Syntax:**
```
Scanner sc = new Scanner(System.in);
int number = sc.nextInt();
```

`Scanner` is a Keyword, `sc` is a class `new` is keyword,
`(System.in);` system take input statment end with `;`
`int` integer datatype, number is a variable, 
`sc.nextInt()` is a function.

User take input store in number variable, variable only store intergers values.

To display text or numbers in console, terminal or screen.
use `System.out.println();`.

```java
System.out.prinfln(1);

System.out.println("Hello, World!")
```

### Basic Syntax 

```java
public class Hello 
{
  public static void Hello() 
  {
    // Rest of code
    System.out.println("Hello");
  }
}
```

### Variables and Types 

Variables are like container as we store something in container,
In Computer, to store value we use variable.

value may of different types:
- `int` Integer Datatype 
- `Strings` Strings Datatype
- `bool` booleans Datatype 
 
Integer numbers start from `0 - 9` (whole numbers). 
Strings are those enclosed with double quotes `""`` alphanumeric (Text and Numbers).
Booleans use in Decision Making (`true` or `false`).

```java
int a; // declare a variable
a = 24; // initial a variable 
```

Declaration and Initialization and Variable

```Java
int a = 234;
```

### Decision Making

If computer need to make decision like OK and Cancel, Yes or No.
`if.. else` conditional statements are used it.

```Java
if (condition) {
  // if condition is true 
} else {
  // else condition is false
}
```

**Example:**
```Java
int a = 1;
int b = 0;
if (a > b) {
  System.out.println("a is greater than b");
} else {
  System.out.println("a is less than b");
}
```

**Output:**
```Java
a is greater than b
```

### Loops

what if you repeat task for 10 or 10,000 times.
Computer can do it in just few seconds.

#### Types of Loops

- while loop 
- do.. while loop 
- for loop

#### while loop

```Java
while (condition) {
  int i = 1; // declare and initial a variable
  i = i + 1; // increment / decrement (i = i -1) 
}
```

#### do.. while loop

```Java
do {
  System.out.println(i);
  i = i + 1;
} while (condition);
```

#### for loop

```Java
for (start; condition; increment/decrement) {
  // rest of code
}
```


**Example:**
```Java
for (int i = 1; i <= 10; i++) {
  System.out.println("Hello, World!");
}
```

```
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
```

### Array 

Arrays just like variable which stores multiple values but same datatype.

```Java
int array_name[] = new int[10];
array_name[0] = 100;
```

`int` is a integer datatype for `array_name` variable.
`[]` using square bracket we can differentiate between variable and array.
variable don't have `[]` square brackets.
`new` is keyword, 

index is unique position of array.
start from 0. first element or value at index 0.

Assign a value to array 
```java 
array_name[0] = 100;
array_name[1] = 101;
array_name[2] = 102;
```

array contain 3 values, first element 100, second element 101, 
third element 102. 

#### Accessing array
```java
int array1 = array_name[0];
```

`100` value from `array_name` array store in `array1`.

accessing using for loop.
```java
for (int i = 0; i < array_name.length; i++) {
  System.out.println([i]);
}
```
