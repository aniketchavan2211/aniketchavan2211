#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--a', '--add', help='help manual')

args = parser.parse_args()
print(args)
