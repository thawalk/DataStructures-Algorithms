def isSubtree(self, s, t):
    def traverse_s(node):
        if not node:
            return False
        
        if node.val == t.val:
            return check_same_tree(node,t) or traverse_s(node.left) or traverse_s(node.right)
        return traverse_s(node.left) or traverse_s(node.right)
    
    def check_same_tree(s,t):
        if (s and not t) or (not s and t):
            return False
        
        if not (s or t):
            return True
        
        if s.val == t.val:
            return check_same_tree(s.left, t.left) and check_same_tree(s.right, t.right)
        return False
    return traverse_s(s)