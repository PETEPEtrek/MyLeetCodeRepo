class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        check = []
        check.append(root.left)
        check.append(root.right)
        while len(check) > 0:
            left = check.pop(0)
            right = check.pop(0)
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            check.append(left.left)
            check.append(right.right)
            check.append(left.right)
            check.append(right.left)
        return True
