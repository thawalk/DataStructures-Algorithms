# Time Complexity = O(n * 2^n)| Space Complexity = O(n * 2^n) 

def powerset(array):
    answer = [[]]
    for elem in array:
        for i in range(len(answer)):
            newSubArray = answer[i]
            answer.append(newSubArray + [elem])
    return answer
