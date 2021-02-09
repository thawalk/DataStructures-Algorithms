# Time Complexity = O(n) | Space Complexity = O(d), where d is the depth of the tree

class Solution:
    def convertBST(self, root):
        runningSum = 0
        def dfs(node):
            nonlocal runningSum
            if not node:
                return
            else:
                dfs(node.right)
                runningSum += node.val
                node.val = runningSum
                dfs(node.left)
        dfs(root)
        return root