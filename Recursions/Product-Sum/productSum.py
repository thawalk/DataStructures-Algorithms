# Time Complexity = O(n), where n is the total number of elements in the array | Space Complexity = O(d), where d is the greatest depth of the array

def productSum(array, depth = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, depth + 1)
        else:
            sum += element
    return sum * depth