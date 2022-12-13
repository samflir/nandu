# receive program file name and input as command-line arguments
# and execute the program with the input
# usage: python nandu.py program input
import sys

# read the program file
program = open(sys.argv[1]).read()

# read the input
input = sys.argv[2]

print(program)
print(input)

