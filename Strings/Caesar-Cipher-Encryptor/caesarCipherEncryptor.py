# <------------- using the ord index ------------>

# Time Complexity = O(n) | Space Complexity = O(n), where n is the number of letters

# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newkey = key % 26
#     for letter in string:
#         newLetters.append(getNewLetter(letter, newkey))
#     return "".join(newLetters)

# def getNewLetter(letter, key):
#     nlc = ord(letter) + key
#     return chr(nlc) if nlc <= 122 else chr(96 + (nlc % 122))

# <------------- Setting your own index ------------>

# Time Complexity = O(n) | Space Complexity = O(n) 
def caesarCipherEncryptor(string, key):
    newLetters = []
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    newkey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newkey, alphabets))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabets):
    newLetterIndex = alphabets.index(letter) + key
    return  alphabets[newLetterIndex] if newLetterIndex <= 25 else alphabets[newLetterIndex % 26]
