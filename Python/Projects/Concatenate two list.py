#!/usr/bin/env python3

list1 = ['g', 'f', 6, 3]
list2 = ['w', 1, 2, 'g']

list3 = list1 + list2
list3 = list(set(list3))

print(list3)

list1.extend(list2)
print(list1)
