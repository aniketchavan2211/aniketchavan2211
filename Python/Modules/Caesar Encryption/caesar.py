#!/usr/bin/env python3

print("Caesar Cipher or 3rd Shift")

alphabet = "ABCDEFGHTJKLMNOPQRSTUVWXYZabcdefghijklmnopqlstuvwxyz"

string_input = input("Enter a string: ")

input_length = len(string_input)

string_output = ""

for i in range(input_length):
  character = string_input[i]
  index = alphabet.find(character)
  new_index = index + 3
  string_output = string_output + alphabet[new_index]

print("Encrypted message: ", string_output)
