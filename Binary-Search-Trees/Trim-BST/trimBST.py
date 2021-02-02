def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
    if not root:
        return 
    if root.val < low:
        return self.trimBST(root.right, low, high)
    if root.val > high:
        return self.trimBST(root.left, low, high)
    else:
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root