# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        def findSumOfPaths(node, path):
            answer = 0
            path = path + str(node.val)
            if node.left == None and node.right == None:
                answer = int(path)
            if node.left != None:
                answer += findSumOfPaths(node.left, path)
            if node.right != None:
                answer += findSumOfPaths(node.right, path)
            return answer
        answer = findSumOfPaths(root, "")
        return answer
