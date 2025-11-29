# WAP to implement NPL tokenization in python

import re

text = "Aaditya lamichhane hello_qorld is the best boy 1"

# 1. Simple whitespace split
tokens_basic = text.split()
## Splits text at every whitespace, keeps punctuation attached to words
## Example output: ['Hello,', 'world!', 'This', 'is', 'NLP', 'tokenization', 'in', 'Python.']

# 2. Regex-based clean tokens
tokens_clean = re.findall(r'\b\w+\b', text)
## Finds all word tokens ignoring punctuation using word boundaries (\b) and \w+ (letters/digits/underscore)
## Example output: ['Hello', 'world', 'This', 'is', 'NLP', 'tokenization', 'in', 'Python']

print("Basic tokens:", tokens_basic)
print("Clean tokens:", tokens_clean)
