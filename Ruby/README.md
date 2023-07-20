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
Ranges may also be used as con