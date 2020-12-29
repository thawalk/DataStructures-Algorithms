# Time Complexity = O(n) | Space Complexity = O(1)

def moveElementToEnd(array, toMove):
    lp = 0
    rp = len(array) - 1
    while lp < rp:
        if array[rp] != toMove and array[lp] == toMove:
            swap(array, rp, lp)
        if array[rp] == toMove:
            rp -= 1
        if array[lp] != toMove:
            lp += 1
    return array

def swap(array, i , j):
    array[i], array[j] = array[j], array[i]