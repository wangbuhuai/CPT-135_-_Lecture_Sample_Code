# Created by Dayu Wang (dwang@stchas.edu) on 2022-05-11

# Last updated by Dayu Wang (dwang@stchas.edu) on 2022-05-11


# "xyz" is a string literal; "s" is a string.
s = "xyz"

# "5" is an integer literal; "x" is an integer.
x = 5

# Using multiple print() statements to show multiple rows of text in the console
print("Hello")
print("World")

"""
# In programming, press the enter key ends a statement.
# It does not move the cursor in the console.
print("Hello
World")
"""

# Using whitespaces in string literals
print("Hello\nWorld")

# Escape character '\'
print("Hello\\nWorld")

# Raw string literal
print(r"Hello\nWorld")

# "end="
print("Hello", end='')
print("World")
print("Hello", end=' ')
print("World")
print("Hello", end='@')
print("World")

"""
# Single quotes versus double quotes
print('Don't do that!')
"""

print("Don't do that!")  # Single quote processed "raw" in double quotes
print('Don\'t do that!')  # Using escape character
