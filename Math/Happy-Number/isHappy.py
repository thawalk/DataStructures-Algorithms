# Time Complexity = O(log(n)) | Space Complexity = O(1)

def isHappy(n):
    slow = getNext(n)
    fast = getNext(getNext(n))
    while slow != 1 and fast != slow:
        slow = getNext(slow)
        fast = getNext(getNext(fast))
    return slow == 1


def getNext(n):
    totalSum = 0
    while n > 0:
        quotient, remainder = divmod(n, 10)
        totalSum += (remainder ** 2)
        n = quotient
    return totalSum