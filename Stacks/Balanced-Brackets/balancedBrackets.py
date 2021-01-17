# Time Complexity = O(n), where n is the number of char in the string | Space Complexity = O(n), storing the values in the stack

def balancedBrackets(string):
    stack = []
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")":"(", "]":"[", "}":"{"}
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
