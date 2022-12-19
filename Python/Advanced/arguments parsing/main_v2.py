#!/usr/bin/env python3
import sys

print(sys.argv)
# print(sys.argv[0]) # filename
# print(sys.argv[1]) # 1 arg
# print(sys.argv[2]) # 2 arg

# Optional arguments / opt

import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['f arg', 'm arg']) # -f and -m is /falg/switch/arguments

print(opts)
print(args)
