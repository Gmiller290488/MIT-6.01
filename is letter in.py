def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    guess = int((len(aStr))/2)
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and (char == aStr):
        return True
    elif len(aStr) == 1 and (char != aStr):
        return False
    else:
        if char == aStr[(guess)]:
            return True
        elif char < aStr[(guess)]:
            return isIn(char, aStr[:guess])
        elif char > aStr[guess]:
            return isIn(char, aStr[guess:])