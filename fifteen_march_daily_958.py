# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        nodes = [root]
        while nodes[0] is not None:
            node = nodes[0]
            nodes.pop(0)
            nodes.append(node.left)
            nodes.append(node.right)

        while nodes and nodes[0] is None:
            nodes.pop(0)

        return len(nodes) == 0
