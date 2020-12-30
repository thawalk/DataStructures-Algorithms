# Time Complexity = | Space Complexity = 

def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(num, threeLargest)
    return threeLargest

def updateLargest(num, threeLargest):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(num, threeLargest, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(num, threeLargest, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(num, threeLargest, 0)

def shiftAndUpdate(num, threeLargest, idx):
    for i in range(idx + 1):
        if i == idx:
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i+1]
