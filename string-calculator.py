# Handle normal numbers & comma (,) between numbers (instead of commas).

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, numbers.split(','))) # Handle normal numbers & comma (,) between numbers (instead of commas).

print(add(""))
print(add("1"))
print(add("1,2,3")) #

###########################################################
###########################################################

# Handle new lines (\n) between numbers (instead of commas).

import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, re.split(r"[,\n]", numbers))) # Handle new lines (\n) between numbers (instead of commas).

print(add("1,2,3,4,5,6,7,8,9,0,10,11,12,12")) # adding any amount of number & getting result

###########################################################
###########################################################

# Handle different delimiters:

def add(numbers: str) -> int:
    if not numbers:
        return 0

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    else:
        delimiter = ",|\n"

    return sum(map(int, re.split(delimiter, numbers)))

print(add("1\n2,3"))
print(add("//;\n1;2"))
print(add("//|\n1|2|3"))


###########################################################
###########################################################

# negative number are not allowed getting exception error

import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    else:
        delimiter = ",|\n"

    num_list = list(map(int, re.split(delimiter, numbers)))

    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")  # raise value exception error

    return sum(num_list)

try:
    print(add("1,-2,3"))
except ValueError as e:
    print(e)
try:
    print(add("//;\n1;-2;-3"))
except ValueError as e:
    print(e)


###########################################################
###########################################################

# Numbers bigger than 1000 should be ignored

import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    else:
        delimiter = ",|\n"

    num_list = list(map(int, re.split(delimiter, numbers)))

    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

    # Ignoring greater than 1000
    return sum(num for num in num_list if num <= 1000)

print(add("2,1001"))
print(add("//;\n1000;2"))
print(add("//;\n1001;2"))

try:
    print(add("1,-2,3"))
except ValueError as e:
    print(e)

try:
    print(add("//;\n1;-2;-3"))
except ValueError as e:
    print(e)