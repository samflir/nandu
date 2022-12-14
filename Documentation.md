* Virtual machine based on bit flipping and loops.
* Uses a 16-bit architecture with a MAR register that allows the pointed address to be modified.
* Hexadecimal digits are used to flip bits.
* Bracketed loops are used for control flow
* Subroutines maybe?
* "#" for comments like Python.
# Instruction set
* Flip bits of MAR
* Flip bits of memory
* Loop: enter if memory is non-zero and repeat until it is zero.
* Antiloop: enter if memory is zero and repeat until it is non-zero.
* Subroutine call
* Exit subroutine
* Input
* Output
* Exit program
# Syntax
## Token separation
Tokens are usually separated from context, even MAR and memory instructions can be written run together because all numeric instructions must have their digits unique and in ascending order. A break in this order is assumed to be a new token, so `.01a23` breaks down into `.01a 23`. If this is not possible, use a space to separate tokens.
Comments run to the end of their line. There are no block comments.
## Flip bits of MAR
To flip a bit of the MAR, write a hexadecimal string of digits after a dot.
Example: `.01a`
## Flip bits of memory
To flip a bit of memory, write a hexadecimal string of digits. There's no syntax for this because it'll be by far the most common operation probably.
Example: `89ab`
## Loop
Loops use square brackets.
Example: `[1[2]3]`
## Antiloop
Antiloops use curly brackets
Example: `{1{2}3}`
## Subroutine call
Subroutine calls start with a capital letter and may contain only lowercase latin letters and hyphen after that.
Example: `Sub`
Subroutines are defined by following the subroutine name with a colon.
Example: `Sub:`
Subroutines end with a semicolon.
Example: `Flip-bit: .00_;`
Subroutines do not run without being called, so they can safely be placed at the top of code. Subroutines can be defined within subroutines, which have only that subroutine as their scope.
## Subroutine exit
Subroutine exit is either implied by a semicolon, or optionally an underscore for early return.
## Input
Input is handled by the ? command, which XORs a character of input to the current memory address.
## Output
Output is handled by the ! command, which outputs the character in memory pointed to by the MAR.
## Exit program
Exit program is the @ command.
