user_string = "1995"

''' Type your code here. '''
validCharacters = [str(i) for i in range(0, len(user_string) - 1)]
def isValid(characters):
    for character in characters:
        if character not in validCharacters:
            return "No"
    return "Yes"
    
print(validCharacters, isValid(user_string))