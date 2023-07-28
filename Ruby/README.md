## Ruby 

### Introduction

Ruby was created in 1993 by Yukihiro Matsumoto of Japan, Pure Object-oriented Programming Language, Open-source and is freely availableon Web. But subject to lincense.

It is also called general-purpose programming language
and interpreted, not complied, ruby is server - side scripting language like python and perl.

CGI (Common Gateway Interface) script can be developed
using ruby.

Ruby can embedded in HTML and can easily connected to DB2, MySQL, Oracle and Sybase.

Ruby is said to follow the principle of least astonishment(POLA).

Meaning that the language should behave in such a way s to minimize confusion for experienced users.

To write ruby program we need and any editor, In Windows, RubyWin (Ruby Integrated Development Environment) is IDE for Windows Or Ruby Development Environment (RDE).

All files will have '.rb' as extension so rename any ruby file as 'file1.rb'

#### Hello World

```ruby
#!/usr/bin/ruby -w
puts "Hello, Ruby!";
```

save as 'test1.rb' and open terminal run program
```
ruby test1.rb
```

***Output**
```
Hello, Ruby!
```

whitespace character such as spaces and tabs are generally ignored in ruby code. execpt when they appear in strings.

Interpretation of this sort produce warnings when the -w option is enabled.

Ruby interprets semicolon ';' and newlines character as the ending of a statement.

However, if ruby encounter operators, such as '+,-,*,/' or blacklash '\' at the end of line, they indicate the continuation of a statement.

Ruby identifiers are case sensitive.

Reserved words cannot be use as constant or variable names. 

```ruby
#!/usr/bin/ruby
BEGIN{
  puts "Initializing the program"
}
puts " This is a main program ";
END {
  puts "End of the program"
}
```

**Output**
```ruby
Initializing the program 
This is a main program 
End of the program 
```

### Variables

Variables are like containers store values like 
strings, integers, floating-point numbers(decimal number). Variables are memory locations. These hold any data to be used by any program.

```ruby
name="John"
```

`name` is a variable that holds and store value `John`.

**Types of Variables**:

1. Global Variables
2. Instance Variables
3. Class Variables
4. Local Variables
5. Constants

#### Global Variables

Variables begin with `$`, Uninitiated global variable have the value nil and produce warnings with the `-w` options.

Assignment to global variables alters the globalisation status

it is not recommended to use global variables.

They make programs cryptic.

#### Instance Variables 

Instance variables begins with `@`.

Uninitialized instance variables have the value nil and produce warnings with the `-w` options.

#### Class variables

Class Variables begin `@@`.
It must be initiated before they can be used in methods definitions.

Referencing an uninitialized class variable produces an error.

Class Variables are shared among descendants of the class or module in which the class variables are defined.

Overriding class variables produces warnings with the `-w` option.

#### Local Variables 

Local variables begins with a lowercase letter or `_`.
The scope of a local variables ranges from class, module, def or from a block's opening braces to its close brace{}. 

When an uninitiated as a call to a method that has no arguments.
It is interpreted as a call to a method that has no arguments. 
The variables start to exist until the end of the current scope is reached. 

The lifetime of local variables is determined when Ruby parses the program. In the above examples are id, name, and addr.

#### Constants 

Constants begins with an uppercase letter.

Constants defined within a class or module can be accessed from within that class or module.

Those defiend outside a class or module can be acccessed globally.

Constants may not be defined within methods.
Referencing an uninitialized constant produces an error.

Making an assignment to a constant that is already initized produces a warning.

#### Pseudo-Variables

They are special variables that have the appearance of local variables but behave like constants.

- `self`: The receiver object of the current method.
- `true`: Value representing true.
- `false`: Value representing false.
- `nil`: Value representing undefined.
- `__FILE__`: The name of the current source file.
- `__LINE__`: Thr current line number in the source file.

You cannot assign any value to these variables.

### Math Operations

An operator is a symbol. It represents an operation to be performed with one or more operands. Operators are the foundation of any programming language. Operators allow us to perform different kinds of operations an operands.

#### Types of Operators

- Arithmetic Operators
- Comparsion Operators 
- Logical Operators 
- Assignment Operators
- Bitwise Operators
- Ternary Operators
- Range Opeartors
- Defined? Operators
- Dot `.` and Double Colon `::` Operators

##### Arithmetic Operators
These are used to perform arithmetic/mathematical Operations an operands.

- Addition(`+`): Operators adds two operands. for ex. x+y.
- Subtraction('-'): Operators subtracts two operands.  for ex. x-y.
- Multiplication(`*`): Operators multiples two operands. for ex. x*y.
- Division(`/``): Operators divides the first operands by the second. for ex. x/y.
- Modulus`(%`): Operators returns the remainder when the first operands is divided by the second. for ex. x%y.
- Exponent(`**`): Operators returns exponential(power)
of the o

##### Comparsion Operators 

Comparsion operators or Relational operators are used for comparison of two values. 

- Equal To(`==`): operators checks whether the two given operands are equal or not. if so, it returns `true`. Otherwise it return false. for eg. `5==5` will return `true`.

- Not Equal To(`!=`): operators checks whether the two given operands are equal or not. if not, it return true. Otherwise, it return `false`. It is the exactly boolean complement of the `==` operators. for eg. `5!=5` will return `false`.

- Greater than(`>`): operators checks whether the first operands is greater than the second operands. if so, it return `true`. Otherwise it return `false`. for eg. `6>5` will return `true`.

- Less than(`<`): operators checks whether the first operands is lesser than the second operand. if so, it returns true. Otherwise it return `false`, for eg. `6<5` will return `false`.

- Combined combination(`<=>`): operators return `0` when first operands equal to second, return `1` when first operands is greater than second operands, and return `-1` when first operator is less than second operands.

- Case Equality Operator(`===`): It will test equality in case statements. 

- `eql?`: This operator returns true if the receiver and argument have both the same type and equal values.
 
- `Equal?` : This operators return true if it the receiver and receiver and arguments have the same object id.

#### Comments 

##### Single-line Comments
Comments are lines of annotation within Ruby code that are ignored at runtime.

A single-line comments starts with # character and they extent form # to the end of the line as follows:

```ruby 
#!/usr/bin/ruby -w
# This is a single line comment.
puts "Hello, Ruby!"
```

When executed, the above program produces the following result:
```ruby 
Hello, Ruby!
```

##### Multi-line Comments 

You can comment multiple lines using `=begin` and `=end` syntax as follows:
```ruby 
#!/usr/bin/ruby 
puts "Hello, Ruby!"
=begin
this is multi-line comment and can spwan as many lines as you like.
But =begin and =end should come in the first line only.
=end
```

When executed, the above program produces the following result:
```
Hello, Ruby!
```

#### Strings & Arrays

A Strings object in Ruby holds and manipulates and arbitrary sequence one or more bytes.

The simplest string literals are enclosed in single quotes(`' " apostrophe character ``).

The text within the quote marks is the value of the string:
```Ruby
'This is single quote string'
"This is double quote string"
```

If you need to place an apostrophe within a single-quoted string literal, precede it with a backslash, so that the Ruby interpreter does not think that it terminates the string:
```Ruby
'Won't you read O'Reilly's book'
'Won\'t you read O\'Reilly's book'
```

1st line cause an error ruby interpreter will get confused between string it will display what is in the single or double quotes.

Expression substitution is a means of embedding the value of any Ruby expression into a string using `#{}`.

**Input**
```Ruby
#!/usr/bin/ruby

x, y, z = 12, 36, 73
puts "The value of x is #{x}"
puts "The sum of x and y is #{x + y}"
puts "The average was #{(x+y+z)/3}"
```

**Output**
```ruby
The value of x is 12.
The sum of x and y is 48.
The average was 40.
```

With general delimited strings, you can create strings inside a pair of matching through arbitrary delimiter characters,

eg. `!`, `(`, `{`, `<` etc... preceded by a percent character(%).
`Q`, `q` and `x` have special meanings.
General delimited strings can be:
```ruby
%{Ruby is fun.} equivalent to "Ruby is fun."
%Q{Ruby is fun.} equivalent to "Ruby is fun."
%q{Ruby is fun.} equivalent to a single-quoted string
%x!ls! equivalent to backtick command output `ls`
```

##### String Built-in Methods 

We need to have an instance of String object to call a String method. Following is the way to create an instance if String object:

```Ruby
new [String.new(str = "")]
```

This will return a new string object containing a copy of str.

Now, using str object, we can all use any available instance methods.

```Ruby
myStr = String.new("THIS IS TEST")
foo = myStr.downcas
puts "#{foo}"
```

**Output**
```
this is test
```

#### Arrays

Ruby arrays are ordered, interger-indexed collection of any object.

Each element in an array is associated with and referred  to by an index.

Array indexing starts at `0`, as in C or Java.

A negative index is assumed relative to the end of the array.

That is, an index of -1 indicates the last element of the array,

-2 is the next to last element in the array, and so on.

##### Creating arrays

There are many ways to create or initialize an array.
```Ruby
names = Array.new(20)
```

The array names now have size or length of 20 elements.

One way is with the newclass methods:
```ruby
names = Array.new
```

#### key:value pair
A Hash is a collection of key-value pairs like this:
"employee" => "salary". It is similar to an Array.

But indexing is done via arbitrary keys of any object type, not an integer index.

The order in which you traverse a hash may seem arbitrary.

It will generally not be in the insertion order.

If you attempt to access a hash with a key that does not exist, the method will return nil.

##### Creating Hashes 

As with arrays, there are a variety of ways to create hashes.

You can create an empty hash with the new class methods:
```ruby
months = Hash.new
```

You can also use new to create a hash with a default value, 
Which is otherwise just nil:
```
months = Hash.new("month")
```
or
```ruby
months = Hash.new"month"
```

We need to have an instance of Hash object to call a Hash method.

As we have seen, following is the way to create an instance of Hash object:
```ruby
Hash[[key =>|< value]* ]
```
or
```ruby
Hash.new [or] Hash.new(obj)
```
or
```ruby
Hash.new { |hash, key| block }
```

This will return a new hash populated with the given objects.

Following are the public hash methods (assuming hash is an array object):
1. **hash == other_hash**
 - Tests whether two hashes are equal.
 - On the basis of whether they have the same number of key-value pairs match the corresponding pair in each hash.
 
2. **hash.[key]**
- Using a key, reference a value from hash.
- If the key is not found, returns a default value.

3. **hash.[key] = value**
- Associates the value given by value with the key given by key.

4. **hash.clear**
- Removes all key-value pairs from hash.

5. **hash.default = obj**
 - Sets a default value for hash.

6.**hash.empty?**
- Tests whether hash is empty (contains no key-value pairs ), returning true or false.

7. **hash.has_value?**
 - Tests whether hash contains the given value.

8. **hash.sort**
- Converts hash to a two-dimensional array containing arrays of key-value pairs, then sorts it as an array.

9. **hash-to-hash**
- Returns hash(self).

Ranges occur everywhere!
January to December, 0 to 9, lines 50 through 67, and so on.

Ruby supports ranges and allow us to use ranges in a variety of ways:
- Ranges as Sequences
- Ranges as Conditions
- Ranges as Intervals

```Ruby
(1..5)       # 1, 2, 3, 4, 5
(1...5)      # 1, 2, 3, 4
('a'..'d')   # 'a', 'b', 'c', 'd'
```

**Ranges as Condition**
Ranges may also be used as conditional expression.

for example,

The following code fragment prints sets of lines from the standard input, where the first line in each set contains the word start and the last line the word ends:

```Ruby
while gets 
  print if /start/../end/
end
```

**Ranges as Intervals**
A final use of the versatile range is as an interval test:

seeing if some value falls within the interval represented by the range.

This is done using `===`, the case equality operator.

Iterators are nothing but methods supported by **collections.**

Objects that store a group of data members are called collections.

In Ruby, arrays and hashes can be termed collections.

Iterators return all the elements of a collection, one after the other_hash

We will be discussing two iterators here, each and collect.

**Ruby each Iterator**

The `each iterator` return all the elements of an array or a hashes

Syntax:
```Ruby
collection.each do |variable|
  code
end
```

It executes code for each element in the collection.

Here, collection could be an array or a ruby hash.

**Ruby collect Iterator**

The collect iterator returns all the elements of a collection.

Syntax:
```Ruby
collection = collection.collection
```

The collect method need not always be associated with a block.

The collect method returns the entire collection, regardless of whether it is an array or a hash.

The collect method is not the right way to do copying between arrays.

There is another method called a clone, which should be used to copy one array into another array.

#### Conditional Statements

We make decisions & predictions daily.

We do selection of action among serveral alternatives.

Every decision-making process produces a final choice.

For example, 

Should I go to college today?
If yes, how?
If not, what should I do then?
And so on..

Ruby offers conditional structures that are pretty conmon to modern languages.

The conditional statments and modifiers avaiable in Ruby are:

1. if..else statement
2. if modifiers
3. unless modifier
4. unless statments
5. case statements

**If..Else statement**

if expressions are used for conditional execution.

The values false and nil are false, and everything else is true.

Ruby uses elsif, not else if or elif.

It executes code if the conditional is true.

If the conditional is not true, code specified in the else clause is executed.

An if expresssion's conditional is separated from code by the reserved word then, a newline, or a semicolon.

Syntax:
```Ruby
code if condtion
```

Executes code if the conditional is true.

**Output:**
```
Debug
```

**Ruby unless statement**

Execute code if conditional is false.

If the conditional is true, the code specified in the else clause is executed.

**Ruby unless modifier**
Syntax:
```Ruby
code unless condtional
```

Executes code if conditional is false.
**Snippet:**
```Ruby

```

**Output:**
```
1 -- Value is set
2 -- Value is set
```

**Case statments**
Compares the expression specified by case.

Also that specified by when using the `===` operator.

It executes the code of the when clause that matches.

The expression specified by the when clause is evaluated as the left operands.

If no when clauses match, cause executes the code of the else clause.

A when statement'e expression is separated from code by the reserved word then, a newline, or a semicolon.

#### Loops 

Suppose you are asked to print your name.

Easy? Obviously, you can.

Now Suppose you are asked to print your name 100 times.

Tiresome but you can do it.

But what if you have to print it n. no. of times.

Difficult?

We can achieve this in Ruby with loops.

Loops in Ruby are used to execute the same block of code a specified number if times.

1. while statment
2. while modifier
3. until statment
4. until modifier
5. for statment
6. break, next, redo, retry statements

**Ruby while Statements**

Executes code while condtional is true.

A while loop's condtional is separated from code by the reserved word do, a newline, backslash `\`, or a semicolon `;``.


**Ruby while Modifier**

Executes code while conditional is true.

If a while modifer follows a begin statement with no rescue or ensure clauses, code is executed once before the conditional is evaluated.

**Ruby until Statements**

Executes code while conditional is false.

An until statement's conditional is separated from code by the reserved word do, a newline, or a semicolon.

**Ruby until modifier**

Executes code while conditional is false.

If a until modifers follows a begin statement with no rescue ir ensure clauese, code is executed once before conditional is evaluated.

#### Advance loop Statements

Executes code once for each element in expression.

A for..in loop is almost exactly equivalent to the following:
```ruby 
(expression).each do |variable[, variable...]| code
end
```

A for-loop's expression is separated from code by the reserved word do, a newline, or a semicolon.

**Ruby break statements**
Syntax:
```ruby 
break
```
Terminates the most internal loop.

Terminates a method with an associated block if called within the block.

**Output:**
```
Value of local variable is 0
Value of local variable is 1
Value of local variable is 3
```

**Ruby next statement**

Syntax:
```ruby 
next
```

Jumps to the next iteration of the most internal loop.

Terminates execution of a block if called within a block.

**Output:**
```
Value of local variable is 2
Value of local variable is 3
Value of local variable is 4
Value of local variable is 5
```

**Ruby redo Statement**

Syntax:
```ruby 
redo
```

Restart this iteration of the most internal loop, without checking loop condtion.

Restart yield or call if called within a block.

The above code will produce the following result and will go in an infinite loop:
```ruby 
Value of local variable is 0
Value of local variable is 0
```

**Ruby retry Statement**
Syntax:
```
retry
```

if `retry` appears in rescue clause of begin expression,

restart from the beginning of the begin body,

if `retry` appears in the iterator, the black, 

or the body of the `for` expression, restarts the invocation of the iterator call.

Argument to the iterator is re-evaluated.

#### Modules 

Reusing small code snippets can make programming easy.

Isn't 

Function let us perform such tasks easily in ruby.

A function is a block of organised, reusable code that is used to perform a single, related action.

Functions provide better modularity for your application, and also a high degree of code reuse.

Ruby methods are very similar to functions in any other programming language.

They are used to bundle one or more repeatable statements into a single unit. 

Methods names should begin with a lowercase letter.

If you begin a method name with a uppercase letter, Ruby might think that it is a constant and hence can parse the call incorrectly.

Methods should be defined before calling them, otherwise Ruby will raise an exception for undefined method invoking.

So, you can define a simple method as follows:
```ruby 
def method_name
  expression 
End 
```

You can represent a method that accepts parameters like this:
```ruby 
def method_name(var1, var2)
  expression 
end
```

Whenever you call the simple method, you write only the method name as follows:
```ruby 
method_name
```

However, when you call a method with parameters, you write the method name such as:
```ruby 
method_name 25, 30
```

The most important drawback to using methods with parameters is that you need to remember the number of parameters whenever you call such methods.

For example, if a method accepts three parameters and you pass only two, then Ruby display an error.

**Return Values form methods**
Every method in Ruby returns a value by default.

This returned value will be the value of the last statement.

for example, 
```Ruby
def test
i = 100
  j = 10
  k = 10
end 
```

This method,when called, will return the last declared variable k.

**Return Statement**

The return statement in ruby is used to return one or more values from a Ruby Method.

Syntax:
```
return [expr[','expr]]
```

If more than two expressions are given, the array containing these values will be the return value.

If no expression is given, nil will be the return value.

##### Class methods

When a method is defined outside of the class, the method is marked is marked as private.

The method defined in the class definition are marked as public by default.

The defaults visibility and the private mark of the method can be changed by public or private of the Module.

Whenever you want to access a method of a class, you first need to instantiate the class.

Then, using object, you can access any member of the class. 

Ruby gives you a way to access a method without instantiating a class.

Let us see how a class method is declared and accessed:
```ruby 
class Accounts
  def reading_charge
  end
  def Accounts.return_data
  end
end
```

See how the method return_data is declared.

It is declared with the class_name followed by a period, which is followed by the name of the method.

You can access this class method directly as follows:
```ruby 
Accounts.return_date
```

**Ruby alias statement**

This gives alias to methods or global variables.

Aliases cannot be defined within the method body.

The alias of the method keeps the current definition of the method, even when methods are overridden.

Making aliases for the numbered global variables ($1,$2,..) is prohibited.

Overriding the built-in global varaibles may cause serious problems.

Syntax:
```
alias method-name method-name
alias global-variable-name
global-variable-name
```

**Ruby undef statement**

This cancels the method definition.

An `undef` cannot appear in the method body.

By using `undef` and `alias`, the interface of the class can be modified independently from the superclass, but notice it may be broke programs by the internal method call to self.
Syntax:
```
undef method-name
```

#### Blocks and Modules

We have seen how Ruby defines methods where you can put a number of statements and then you call that method.

Similarly, Ruby has a concept of Block.

A Block consists of chunks of code.

You assign a name to a block.

The code in the block is always enclosed within braces`{}`. 

A block is always invoked from a function with the same name as that of the block.

This means that if you have a block with the name test, then you use the function test to invoke this block.

You invoke a block by using the `yeild` statements.

Syntax:
```Ruby 
block_name {
  statement1
  statement2
  ...
}
```
When you are driving.

If you see the yield sign, you let other vehicles pass through before you enter the road.

In Ruby, the yield keyword yield the flow of control to the code in the block.

So, the code in the block is executed and the execution continues after the line containing the yield.

**Output:**
```
You are in the method
You are in the block
You are again back to the method
You are in the block
```

you have seen how a block and method can be associated with each other.

You normally invoke a block by using the yield statemnet from a method that has the same name as that of the block.

This example is the simplest way to implement a block.

You call the test block by using the yield statement.

Evey Ruby source file can declare blocks of code to be run as the file is being loaded(the BEGIN blocks).

After the program has finished executing (the END blocks).

A program may include multiple BEGIN and END blocks.

BEGIN blocks are executed in the order they are encountered.

END blocks are executed in reverse order.

**Modules**

Modules are a way of grouping together methods, classes, and constants.

Modules give you two major benefits.

Modules provide a `namespace` and prevent name clashes.

Modules implement the `mixin` facility.

Modules define a namespace, a sandbox in which your methods and constants can play without having to worry about being stepped on by other methods and constants.

Syntax:
```Ruby
module identifiers
  statement1
  statement2
  ...
end
```
Module constants are named just like class constants, with an initial uppercase letter.

The method definition look similar, too:

Modules methods are defined just like class methods.

**Ruby require statement**

The `require` statement is similar to the include statement of C and C++ and the import statement of Java.

If a third program wants to use any defined module,

it can simply load the module files using the Ruby require statement.

Syntax:
```ruby 
require filename
```
Here, it is not required to give `.rb` extension along with a file name.

**Ruby include statement**
You can embed a module in a class 

To embed a module in a class, you use the include statement in the class.
Syntax:
```ruby 
include modulename
```
If a module is defined in a separate file,

then it is required to include that file using require statement before embedding the module in a class.

**Mixins in Ruby**
Before going through this section, we assume you have the knowledge of Object Oriented Concepts.

When a class can inherit features from more than one parent class, the class is supposed to show multiple inheritance.

Ruby does not support multiple inheritance directly.

But Ruby Modules have another wonderful use.

At a stroke, they pretty much eliminate the need for multiple inheritance, providing a facility called a mixin.

Mixins give you a wonderfully controlled way of adding functionality to classes.

However, their true power comes out when the code in the mixin starts to interacts with code in the class that uses it.

#### File Managements

Ruby provides a whole set of I/O- related methods implementated in the kernel module.

All the I/O methods are derived from the class IO 

The class IO provides all the basic methods, such as read, write, gets, puts, readline, gets, and printf.

**puts**
The `puts` statement instruct the program to display the value stored in the variable.

This will add a new line at the end of each line it writes.

**gets**
The `gets` statement can be used to take any input from standard screen called STDIN i.e. from the console.

**putc**
unlike the `puts` statement, which outputs the entire string onto the screen,

the putc statement can be used to output one character at a time.

**print**
The `print` statement is similar to the `puts` statement. 

The only difference is that the puts statement goes to the next line after printing the contents.

Whereas with the print statement the cursor is positioned on the same line.

**Opening and Closing files**
Until now, you have been reading and writing to the standard input and output.

**File.new Method**
You can create a `File` object using `File.new` method for reading, writing, of both, according to the mode string.

Finally, you can use `File.close` method to close that file.

**File.open**
You can use `File.open` method to create a new file object and assign that file object to a file.

However, there is one difference between File.open and File.new methods.

The File.open method can be associated with a block,

**sysread method**
The method `sysread` is used to read the contents of a file.

You can open the file in any of the modes when using the method sysread.

This statement will output the first 20 characters of the file.

The file pointer  will now be placed at the 21st character in the file.

**syswrite method**
You can use the method syswrite to write the content into a file.

You need to open the file in write mode when using the method syswrite.

This code statement will write `ABCDEF` into the file.

**The IO.readlines Method**
The class File is a subclass of the class IO.

The class IO also has some methods, which can be used to manipulate files.

One of the IO class method is `IO.readlines`.

This method returns the contents of the file line by line.

**Renaming and Deleting files**
You can `rename` and `delete` files programmatically with Ruby with the `rename` and `delete` methods.

Follwing is the example to rename an existing file `test1.txt`:
```ruby 
# Rename a file from test1.txt to test2.txt
File.rename("test1.txt", "test2.txt")
```

**Deleting an Existing file:**
```ruby 
# Deleting file test2.txt
File.delete("test2.txt")
```