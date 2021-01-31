#ISBN: 3-598-21508-8


def is_valid(isbn):

    
    #strip ISBN of hyphens to get a string consisting only of digits
    hyphenStrippedString = "" #consider using the .replace method
    for element in isbn:
        if element.isalnum():
            hyphenStrippedString += element

    #ISBN valid if string contains 10 chars, otherwise invalid
    if len(hyphenStrippedString) == 10:
      
        stringSplit = list(hyphenStrippedString)

        #create list of integers based on processed string for later use in formula
        digitList = []
        indexCounter = 0
        for digit in stringSplit:
            if digit.isalpha():
                if digit == "X" and indexCounter == 9:
                    # add 10 to the list if progam encountes x at indexposition 9 (index starts at 0)
                    digitList.append(10)
                else:
                    return False
            else:
                digitList.append(int(digit))

            indexCounter += 1

        #multiple assignment of integer values
        a, b, c, d, e, f, g, h, i, j = digitList

        #check validity of ISBN
        checkValidity = formula(a, b, c, d, e, f, g, h, i, j)
        if checkValidity != 0:
            return False
        return True
  
    else:
        return False

def formula(a, b, c, d, e, f, g, h, i, j):
    return (a * 10 + b * 9 + c * 8 + d * 7 + e * 6 + f * 5 + g * 4 + h * 3 + i * 2 + j * 1) % 11


