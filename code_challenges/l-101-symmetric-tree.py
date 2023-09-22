"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        if not (root.left or root.right):
            return True
        
        if not (root.left and root.right):
            return False

        if root.right.val == root.left.val:
            return self.checkIfTwoSubtreesAreMirror(root.left,root.right)
        return False
    
    def checkIfTwoSubtreesAreMirror(self, left, right):
        if not (left or right):
            return True
        
        if not (left and right):
            return False
        
        if left.val==right.val:
            return self.checkIfTwoSubtreesAreMirror(left.left, right.right) and self.checkIfTwoSubtreesAreMirror(left.right, right.left)
        return False