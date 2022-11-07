![ JavaScript ](https://github.com/aniketchavan2211/aniketchavan2211/blob/master/Images/js.png)

## JavaScript

### Introduction

 **Javascript** is flexiable language that powers dynamic websities and apps.

 JavaScript is a high-level, often just-in-time compiled
 language that conforms to the ECMAScript standard. It has
 dynamic typing, prototype-based object-orientation, and
 first-class functions. It is multi-paradigm, supporting
 event-driven, functional, and imperative programming styles.
 It has application programming interfaces (APIs) for working
 with text, dates, regular expressions, standard data structures
 , and the Document Object Model (DOM).

 **ECMAscript** is a JavaScript standard meant to ensure the
 interoperability of web pages across different web browsers.

 ECMA-262 or the ECMAScript Language Specification defines the
 ECMAScript Language, or just ECMAScript. ECMA-262 only
 specifies language syntax and semantics of the core API, such
 as Array, Function, and globalThis, while valid implementations
 of JavaScript add their own functionality like input/output or
 file system handling.

### Comments

 JavaScript comments can be used to explain JavaScript code,
 and to make it more readable.

 JavaScript comments can also be used to prevent execution,
 when testing alternative code.

#### Single-line Comment

 Single line comments start with `//`.

 Any text between `//` and the end of the line will be ignored
 by JavaScript (will not be executed).


 ```js
 // This is Comment
 ```
#### Mutli-line Comments

 Multi-line comments start with `/*` and end with `*/`.

 Any text between `/*` and `*/` will be ignored by JavaScript.

 ```js
 /*
 This
 is
 multi-line
 comments
 */
 ```

### Variables and Types 

Variables are like containers we can store values in them,and use any time need.

```
var variable_name = "value"
var  name = "Alex"
```

To define variable `var` keyword is use.
`name` is variable name `=` is to assigned a variable a name
`"Alex"` is a value of name variable.
texts and numbers enclosed with double quotes `""` are
strings.

to assigned variable a number
```js
var age = 18 
```
now, To define varaibles we use,

- `let`
- `const`

`let` keyword is use when we need to update or change value of variable .

```javascript
let name = "Alex";
name = "Alexa";
```

to update variable don't use `let` keyword again
it will throw an error.

What if you don't want to change values of variables.
`const` keyword is use, means constant never change/update variable values.

javascript is case-sensitive language. `NAME` and `name`
is different.

```
const age = 1;
```

end the statement with `;` semicolon.

storing `true` and `false`.
```js
let name = true;
```

```js
let name = "true"
```
Both are differnt first one true boolean value but second one is string.

### Math calculation
```js
let first_num = 1;
let second_num = 2;

let result = first_num + second_num;
console.log(result) // use to on console
// document.write use to display on html page
```

### Operator

#### Arithmetic Operator
- Addition `+`
- Substraction `-`
- Multiplication `*`
- Division `/`
- Modulus (Division Remainder) `%`

#### Comparison Operator
- Equality  `==`
- InEquality `!=` 

#### Logical Operator
- and `&&`
- or  `||`

```js
let first_num = 1;
let second_num = 2;

result = first_num == second_num // false
result = first_num != second_num // true
result = first_num == second_num and first_num != second_num // false
result = first_num == second_num or first_num != second_num // true 
```

### Decision making

**Syntax:**
```js
if (condition) {
  // code to be executed
}else {
  // code to be executed
}
```

**Example:**
```js
let x = 1;
let y = 2;

if (x > y) {
  document.write("X is greater than Y")
}else {
  document.write("X is less than Y")
}
```

**Output:**
```js
X is less than Y 
```

### Array 

```js
let array_items = ["item1", "item2", "item3"]
```

This ia invalid, storing different datatype values in same array throw an error.

```js
let array = ["text", 1, 1.02];
// instead do This

let array_string = ["Alex", "Alexa", "McQueen", "Matter"];
let array_num = [1, 2, 3, 4, 5];

```

#### Accessing Array 

Index is position of string or number
```js
let array_name = ["item1", "item2"];

document.write(array_name[index]);
document.write(array_name[0]); // item1
document.write(array_name[1]); // item2
```

```js
let students = ["Alex", "Alexa", "Swanand", "Amar"];

document.write(student[0]); // Alex
document.write(student[1]); // Alexa
document.write(student[2]); // Swanand
document.write(student[3]); // Amar
```

### Loops

- for Loops
- do.. while loop 
 
#### for loop 

**Syntax:**
```js
for (initial value; condition; increment) {
  // rest of code
}
```

**Example:**
```js
let i;
for (i = 0; i<10; i++)  {
  document.write("Hello, World!");
}
```

#### do.. while loop

loops executed once then checks the condition for 
second time if false then loop terminate
or keeps running until condition no longer satified

**Syntax**
```js
do {
  // code to be executed
  i = i +1 // increment
}while (condition);
```

**Example:**
```js
let i = 1;
do {
  document.write("Hello, World");
  i = i + 1
}while (i < 10);
```

### Dialog Boxes

- Alert Box
- Prompt Box
- Confirm Box

#### Alert Box

```js
alert("Alert Waring Message");
```

#### Prompt Box

```js 
prompt("Prompt Message"); 
prompt("What's is your name"); 
```

#### Confirm Box

```js 
confirm("Confirm Message");
```

### Functions

**Syntax:**
```js
function function_name(parameter1, parameter2) {
  // Code to be Executed
}
```

Calling function when needed.

```js
function_name(parameter1, parameter2);
```

**Example:**
```js
function add(num1, num2) {
  let result = num1 + num2;
  document.write(result);
}

add(3, 4);
```

**Output:**
```js
7
```