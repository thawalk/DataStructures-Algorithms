def findClosestLeaf(root, k):
    if not root: return
    graph = defaultdict(list)
    leaves = set()
    def traverse(node):
        if not node.left and not node.right:
            leaves.add(node.val)
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            traverse(node.left)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            traverse(node.right)  
    traverse(root)
    
    queue = deque([k])
    visited = set()
    while queue:
        l = len(queue)
        for i in range(l):
            node = queue.popleft()
            if node in leaves:
                return node
            if node not in visited:
                queue += graph[node]
                visited.add(node)