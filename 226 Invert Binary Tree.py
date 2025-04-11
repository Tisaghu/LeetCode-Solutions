# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Call function recursively on left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return current node
        return root