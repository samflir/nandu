def tokenize(program):
    # Return a list of every token in the program as a string, ignoring whitespace and comments
    counter = 0 # This is the index of the current character in the program
    tokens = [] # This is the list of tokens that will be returned

    while counter < len(program):
        # First skip whitespace
        while program[counter].isspace():
            counter += 1
        # Now check for comments
        if program[counter] == '#':
            # Skip the rest of the line
            while program[counter] != '\n':
                counter += 1
            continue
        # Now check for single character tokens
        if program[counter] in '[]{};_!?@':
            tokens.append(program[counter])
            counter += 1
            continue
        # Now check for address tokens, these start with .
        if program[counter] == '.':
            tokenLength = getLength(program, counter + 1)
            tokens.append(program[counter:counter + tokenLength + 1])
            counter += tokenLength + 1
            continue
        # Now check for memory tokens, these are lowercase hexadecimal numbers
        if program[counter] in '0123456789abcdef':
            tokenLength = getLength(program, counter)
            tokens.append(program[counter:counter + tokenLength])
            counter += tokenLength
            continue
        # raise exception
        raise Exception('bad program')
    return tokens

def getLength(program, counter):
    # get length of strictly increasing unique hexadecimal numbers
    highestDigit = program[counter] #current highest digit
    if highestDigit not in '0123456789abcdef':
        raise Exception('bad program') #this will usually occur with dots, best to be on the safe side
    tokenLength = 1 #length of token
    counter += 1 #increment counter
    while counter < len(program) and program[counter] in '0123456789abcdef':
        if highestDigit < program[counter]:
            highestDigit = program[counter]
        else:
            break
        tokenLength += 1
        counter += 1
    return tokenLength
    