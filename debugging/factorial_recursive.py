#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
