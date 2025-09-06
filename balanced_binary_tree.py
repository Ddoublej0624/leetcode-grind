# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def maxHeight(root):
            if not root:
                return 0
            return 1 + max(maxHeight(root.left), maxHeight(root.right))

        nodeBalanced = abs(maxHeight(root.left) - maxHeight(root.right)) <= 1
        
        return nodeBalanced and self.isBalanced(root.left) and self.isBalanced(root.right)
