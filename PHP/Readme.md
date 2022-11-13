## PHP

### Introduction 

In 1995, PHP was created by Rasmus Lerdorf, PHP stands for HyperText Preprocessor.
originially named as Personal Home Page. Php is a general-purpose language work with HTML

- Server-side scripting
- Command-line scripting
- Writing Desktop Application

### Main Components
- **MVC architecture** : it's means Model-View Controller. It can help you manage your code
and separate the model. view and controller files.

- **Frameworks** : PHP boosts an enormous number of Frameworks
build to help developers with everything from buidling simple pages to 
organizing complex projects.

- **Web-Server** : PHP mainly works on webserver software and uses the Apache server.

- **PHP Parser** :  Parser helps in parsing the PHP instructions to HTML code 
and then sends it to a web browser to display the content.

- **Autosuggest** : The components are ready to use to implement the search
 form with the auto-suggest feature using PHP and database MySQL.

- **Filters** :  in PHP, **Filters** are used to validate the data using 
the filter function.

- **System Functions** : the system, function are performed to open 
the file.

### Comments

Comments are used to ignored by php interpreter, so code can comment or we can describe the code can comment it. so others programmers will know to we know that code what is does.


```PHP
// Single-Line Comments
```

To comment multiple ;ines we used `/*` at beginning and `*/` at the end.

```
/* 
Multi 
Line
Comments
*/
```

### Hello World

**Syntax:**
```PHP
<?php

?>
```

`<?php ` is opening tag and `?>` is closing tag
save file as `index.php` host on web server.

**PHP Development server:**
```bash
php -S 127.0.0.1:8000 -t <directory root>
```

**Example:**
```PHP
<?php 
echo "Hello World!";
?>
```

`echo` is command or function use to display output on screen.
at last of statements end with `;` (semicolon).

**Example:**
```php
<!DOCTYPE html>
<html>
  <body>
    <?php 
      echo "Hello";
     ?>
  </body>
</html>
```

### Variable and DataTypes 

Variables are like containers or box to store value.
to store text or numbers, etc we use varaibles.

to declared variable first before named `$` dollor sign,
then `variable_name`, `=` assignment operator, and value.
strings those enclosed with `"double"` or `'single quotes'`.
values can be numbers (Don't use quotes for numbers, quotes numbers are strings. you can't manipulate.)

```
$variable_name = "value";
$num = 1
echo "specify $variable_name";
```

assign `1` to `num`, `1` is numeric value assign to variable name `num`.

#### DataTypes

##### Scalar Types

These include integers, strings, booleans, and float
which are the most used and simplest datatypes in PHP.

- integers `(0-9)`
- floating point numbers / decimal numbers (`1.5`, `5.0`, etc)
- strings are those who are enclosed with double quotes `""`, every text, chaarcter,
words, and numbers are strings. (`"Text"`, `"12"`)
- booleans `true` and `false` are two values. use in decision making, conditional statements.

##### Compound Types 

These include arrays and objects which are considered more 
complex,as they hold more than a single value.

arrays are those who store multiple values in one variable. list of values.

##### Special Types 

This includes somethings called a Resource is technically not
a datatype, because it points to an outside reference. 
it is a special variable that holds references to resource
external to PHP. it also includes NULL that holds no value at all.

### Operators 

#### Arithmetic Operators

```php
<?php
$x = 43:
$y = 3:

echo($x + $y), "<br>"; // Addition
echo($x - $y), "<br>"; // Substraction
echo($x * $y), "<br>"; // multiply
echo($x / $y), "<br>"; // division
echo($x % $y), "<br>";  // modulous
?>
```

**Output:**
```
64
56
240
15 
0
```

**Concatenate operator**

To join two variable use Concatenate operator period / dot / full stop `.`.

**Example:**
```php
$n = 1;
$a = 2;
$play = $n.$a;
echo $play;
```

#### Assignment Operators

| Operators |  Description |
| --------- | ------------ |
| a = b | The variable  on the left gets the value of the variable on the right |
| a += b |  Same as a=a+b. Adds the value on the left of the operand to the value on the right |
| a -= b |  Same as a=a-b. Subtracts the value on the left of the operand to the value on the right |
| a \*= b |  Same as a=a\*b. Multiple the value on the left of the operand to the value on the right |
| a /= b |  Same as a=a/b. Divide the value on the left of the operand to the value on the right |
| a %= b |  Same as a=a%b. Display the modulous of the value on the left of the operand to the value on the right |

#### Comparsion Operators

| Operators | Name |
| --------- | ---- |
| `==` | Equal to |
| `!=`, `<>` | Not Equal to |
| `===` | Identical to |
| `!==` | Not Identical to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `<` | less than |
| `<=` | less than or equal to |

#### Logical Operators

| Operators | Name |
| --------- | ---- |
| `and` | And |
| `or` | Or |
| `xor` | Xor |
| `&&` | And |
| `||` | Or |
| `!` | Not |

```php
$x = 200;
$y = 150;

echo ($x == 200 || $y == 100), "<br>";
echo ($x == 200 && $y == 150), "<br>";
echo ($x == 200 and $y == 150), "<br>";
echo ($x == 100 or $y == 150), "<br>";
echo ($x == 200 xor $y == 100), "<br>";
```

**Output:**
```
replace echo with var_dump() gives bool values in true and false.


0 = false 
1 = true

1 // true
1 // true
1 // true
1 // true
1 // true
```

#### Operatror Precedence

```
3 + 6 * 3 
```

according to Operator Precedence output be `21`.
here, why
```
3 + (6 * 3)
3 + 18
21
```

because multiple operator.

operator are:
```
/ * %
+ -
< <= => >
== === !=
&&
||
= += -= *= /= %= .=
and
xor
or 
```

### Decision making

What if Computer need to take decision, we can specify the condition, if condition is true then then that code will executed or else condition is false then specify task will formed. 

#### if..else

**Syntax:**
```php
if (condition) {
  // condition is true
} else {
  // condition is false
}
```

#### if.. else if.. else

**Syntax:**
```php
if (conditon1) {
  // conditon1 is true
} else if (condition2) {
  // condition2 is true
} else if (condition3) {
  // condition3 is true
} else {
  all conditon are false
}
```

#### Switch case

**Syntax:**
```php

switch (expression/variable) {

  case 'value1':
    // code to be executed
    break;
    
  case 'value2':
    // code to be executed
    break;
    
  case 'value3':
    // code to be executed
    break;
    
 default:
   // code to be executed 
}
```

### Loops

What if we need of repeating same task many times so, we use loops to performed.

#### for Loops

if we know how many times we need to executed the task we used for loop.

**Syntax:**
```php
for (initialization; condition; increment/decrement) {
  // code to be executed  
}
```

#### while Loops

what if don't know how many times loop will run, but know the condition, make a use of while loop.

**Syntax:**
```php
$i = 1;
while (condtion) {
  // code to be executed
  i = i + 1; // increment
}
```

#### do.. while Loops

do.. while loop will executed atleast once.

**Syntax:**
```php
do {
  // code to be executed;
} while (condition);
```

### Arrays 

Arrays are variable that store multiple values but same data type.

**Syntax:**
```php
array_name = array("Name", "Age", "Address");

echo $array_name[0];
echo $array_name[1];
echo $array_name[2];
```

**Output:**
```php 
Name
Age
Address
```

#### Types of Array

-  Indexed/numeric arrays: arrays with a numeric index.

-  Asssociative arrays: array with named keys.

```
$arr = array("Text" => "Hey", "Name" => "John")

echo $arr["Text"]
```

`Text` and `Name` is a keys and `Hey` and `John` is values. 

-  MultiDimensional arrays: arrays that hold one or more arrays.

```php
$employee = ['name' => 'Sam', 'sports' => ['Tennis', 'Soccer']];

echo $employee['sport'][0]
```

**Output:**
```
Tennis
````

#### foreach Loops

display values using foreach loop.

```
foreach ($array as $value) {
  // code to be executed
}
```

### Functions

once once code is written, no need to write code again.

**Syntax:**
```php
function function_name (parameter1, parameter2) {
  // code to be executed;
}

function_name(parameter1, parameter2); // call / invoke a function
```