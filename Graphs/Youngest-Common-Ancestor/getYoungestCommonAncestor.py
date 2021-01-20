class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Time Complexity = O(d) , where d is the depth of the the ancestral tree | Space Complexity = O(1)

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne, depthTwo = getDepth(descendantOne), getDepth(descendantTwo)
    if depthOne < depthTwo:
        return helper(descendantOne, descendantTwo, depthTwo - depthOne)
    elif depthTwo < depthOne:
        return helper(descendantTwo, descendantOne, depthOne - depthTwo)
    else:
        return descendantOne

def getDepth(node):
    depth = 0
    while node is not None:
        depth += 1
        node = node.ancestor
    return depth

def helper(higherNode, lowerNode, diff):
    counter = 0
    while counter < diff:
        lowerNode = lowerNode.ancestor
        counter += 1
    while lowerNode != higherNode:
        lowerNode = lowerNode.ancestor
        higherNode = higherNode.ancestor
    return lowerNode
