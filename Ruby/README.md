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