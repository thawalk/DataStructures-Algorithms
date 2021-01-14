# Time Complexity = O(wnlog(n) + nwlog(w)), where w is the number of words, and n is the length of the longest word | Space Comlexity = O(wn) 

def groupAnagrams(words):
    if len(words) == 0:
        return []

    sortedLettersList = ["".join(sorted(word)) for word in words]
    indexList = [index for index in range(len(words))]
    indexList.sort(key= lambda x: sortedLettersList[x])
    
    finalResult = []
    currentGroup = []
    currentAnagram = sortedLettersList[indexList[0]]
    for index in indexList:
        word = words[index]
        sortedLettersWord = sortedLettersList[index]
        
        if sortedLettersWord == currentAnagram:
            currentGroup.append(word)
            continue

        finalResult.append(currentGroup)
        currentGroup = [word]
        currentAnagram = sortedLettersWord
    finalResult.append(currentGroup)
    return finalResult
