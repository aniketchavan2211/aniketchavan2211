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















