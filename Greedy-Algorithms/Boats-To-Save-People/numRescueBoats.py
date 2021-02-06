def numRescueBoats(people, limit):
    people.sort()
    leftP = 0
    rightP = len(people) - 1
    result = 0
    while leftP <= rightP:
        result += 1
        if people[leftP] + people[rightP] <= limit:
            leftP += 1
        rightP -= 1
    return result