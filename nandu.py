# receive program file name and input as command-line arguments
# and execute the program with the input
# usage: python nandu.py program input
import sys
from tokenizer import *

# read the program file
program = open(sys.argv[1]).read()

# read the input
input = sys.argv[2]

# tokenize the program
tokens = tokenize(program) # This creates a list of tokens for parsing

# parse subroutines
#subroutines = parse_subroutines(tokens) # This creates a nested dictionary of subroutines for use in execution

print(tokens)