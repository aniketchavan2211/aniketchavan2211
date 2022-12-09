## javascript

**javascript** is a cross-platform programming language, which means that it can run on multiple platforms like Windows, macOS and Linux. It is free and open-source.

- Language type: Programming
- Extension: `.js`
- Uses type: Web dev, Games dev, Application dev, Script, etc.
Frameworks: nodejs, angularjs, react, etc.

### Internal 

```
<!doctype html>
<html>
<head>
  <script>
  
    console.log("Hello");
    var a = 5;
    var b = 1;
    var c = (a + b);
    console.log(a + b);
 
  </script>
</head>
</html>
```

### Inline

```index.html
<head>
 <script>
   function openpage(){
     document.getElementById('#para');
   }
 </script>
</head>
<body>
 <p id="para" onclick="openpage()">
   
 </p>
</body>
```
### External 

create `script.js` file in same directory and link file to `index.html`.
```index.html
<head> 
 <script type="text/javascript" src="script.js"> </script>
</head>
```
  
### Syntax

- js is case-sensitive, num and Num are both different variables
- using `console.log("Hello");` statement will prints on console of browser, not on webpage, instead use `document.write("Hello");` this will print on html web page.
- `console.log()` and `CONSOLE.log()`  are two different commands, first one will execute properly but second one will not execute, in js `CONSOLE.log` is not a function or command.

```script.js
function func_Name(parameters) {
  body of code;
};
```

### Comments

Comments are ignored by compiler, comments will not execute, so you comments any text or numbers, use for developers, etc. comments can explained the code. 


#### One-line comments

comment only one line.
```javascript
// one-line commments
```

#### Multiple line Comments
start: `/*`
end: `*/`

```javascript
/* Multiple 
line 
Comments */
```

### Keywords and Identifiers

Reserved keywords:  console.log(), document.write(), etc that are already defined function or built-in functions.

identifiers: user-defined function, function create by user, developers, etc.

`var` is reserved keyword to defined variables, variable_name dont use reserved keyword its throw an error always use decriptive varaiable name like if you want to store number then use 
`num`, `number`, etc, end the statement with `;` semicolon.

```js
var var_Name = 1;

function xyz(parameter1){
  // body
};
```

function is keyword and xyz is a identifier.


### statement & typecasting

statement are codes, commands, functions 
```js
document.write();
```

document.write() is a built-in function used to print text on webpage, `;` semicolon are end   of statements.

typecasting means converting datatype, decimals numbers are floating-points numbers(1.53, 6.34), integers are normal numbers (1, 757, 345).

`typeof` built-in function used to print datatype

```js
function sample(){
  document.write("Hello")
};

// call function
sample();
```

```js
// datatype

var integer = 1;
var floating-point = 1.3;
var string = "Hello";
var bool = true;
var array_name = ["value1", "value2"]

document.write(typeof(integer)); // number
```

### typecasting

```js
var a = 86
document.write(46 + a) // 125

var b = String(a) // typecasting a variable as string(text "86" ) 
document.write(46 + a) // 4686 a is string and string and numbers can't be added.
```







