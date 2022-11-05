#!/usr/bin/env python3

dict1 = {'key1': 'value1', 'key2':'value2'}
dict2 = {'key3':'value3', 'key4':'value4'}

# print(dict1 | dict2)
# print({**dict1, **dict2})

dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)
