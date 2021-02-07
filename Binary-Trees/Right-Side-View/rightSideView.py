# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        
        answer = []
        nextLevel = deque([root,])
        
        while nextLevel:
            currentLevel = nextLevel
            nextLevel = deque()
            
            while currentLevel:
                currentNode = currentLevel.popleft()
                
            
                if currentNode.left:
                    nextLevel.append(currentNode.left)
                if currentNode.right:
                    nextLevel.append(currentNode.right)
            
            answer.append(currentNode.val)
        return answer