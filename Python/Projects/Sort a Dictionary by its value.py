#!/usr/bin/env python3

dict = {'John':13, 'Lisa': 43, 'Tom': 93}

sort_keys_values = sorted(dict.items(), key = lambda x : x[1])
print(sort_keys_values)

sort_values = sorted(dict.values())
print(sort_values)
