def killProcess(self, pid, ppid, kill):    
    parentChildMap = {}
    for i in range(len(ppid)):
        if ppid[i] not in parentChildMap:
            parentChildMap[ppid[i]] = [pid[i]]
        else:
            parentChildMap[ppid[i]].append(pid[i])
    
    queue = [kill]
    answer = []
    while queue:
        pop = queue.pop()
        answer.append(pop)
        if pop in parentChildMap:
            for elem in parentChildMap[pop]:
                queue.append(elem)
        
        
    return answer