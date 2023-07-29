#!/usr/bin/ruby

# puts "Hello, Ruby!"

# puts "What's your name?"
# name = Aniket



# puts "\nHi #{name}"

class Calculator
  def add(a, b)
    a + b
  end
  
  def sub(a, b)
    a - b
  end

  def mul(a, b)
    a * b
  end

  def div(a, b)
    raise "Cannot divide by zero" if b.zero?
    a / b.to_f
  end
end 

calculator = Calculator.new

puts "Ruby Calculator\n"

loop do 
  puts "Please enter first number: "
  num1 = gets.chomp.to_f

  puts "Please enter second number: "
  num2 = gets.chomp.to_f

  puts "$elect an opearation(+, -, *, /): "
  operator = gets.chomp

  result = case operator
           when "+"
             calculator.add(num1, num2)
           when "-"
             calculator.sub(num1, num2)
           when "*"
             calculator.mul(num1, num2)
           when "/"
             calculator.div(num1, num2)
           else
             "Invalid operator"
           end

  puts "Result: #{result}"

  puts "Do you want to perform another calculation? (yes/no)"
  continue = gets.chomp.downcase
  break if continue != "yes"
end
