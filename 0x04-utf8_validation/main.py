#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

print("-" * 10)

print(f'345 = {345:b}\n467 = {467:b}')
print(validUTF8([345, 467]))

print(f'235 = {235:b}\n140 = {140:b}')
print(validUTF8([235, 140]))
