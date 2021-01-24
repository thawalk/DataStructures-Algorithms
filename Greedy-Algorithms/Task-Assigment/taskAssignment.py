# Time Complexity = O(nlogn), sorting is the reason | Space Complexity = O(n), storing all the values in a map

def taskAssignment(k, tasks):
    answer = []
    indicesMap = getIndices(tasks)
    sortedTasks = sorted(tasks)
    for idx in range(k):
        # from the left
        task1Duration = sortedTasks[idx]
        task1Index = indicesMap[task1Duration].pop()

        # from the right
        task2Duration = sortedTasks[len(sortedTasks) - 1 - idx]
        task2Index = indicesMap[task2Duration].pop()

        answer.append([task1Index, task2Index])
    return answer



def getIndices(tasks):
    indicesMap = {}
    for idx in range(len(tasks)):
        if tasks[idx] not in indicesMap:
            indicesMap[tasks[idx]] = [idx]
        else:
            indicesMap[tasks[idx]].append(idx)
    return indicesMap