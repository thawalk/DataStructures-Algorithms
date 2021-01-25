# Time Complexity = O(4^n * n) | Space Complexity = O(4^n * n)

def phoneNumberMnemonics(phoneNumber):
    result = []
    mnemonic = ['0' for _ in range(len(phoneNumber))]
    phoneNumberHelper(0,phoneNumber,mnemonic,result)
    return result

def phoneNumberHelper(idx, phoneNumber, mnemonic, result):
    if idx == len(phoneNumber):
        mnemonicString = ''.join(mnemonic)
        result.append(mnemonicString)
    else:
        digit = phoneNumber[idx]
        letters = DIGITS[digit]
        for letter in letters:
            mnemonic[idx] = letter
            phoneNumberHelper(idx+1, phoneNumber, mnemonic, result) 



DIGITS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"],
    "6": ["m","n","o"],
    "7": ["p","q","r","s"],
    "8": ["t","u","v"],
    "9": ["w", "x","y","z"],    
}