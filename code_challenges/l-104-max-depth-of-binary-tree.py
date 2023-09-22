"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

class Solution:
    """
        - DFS
        - Recursion
        - O(n)
    """
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepthIterativeDFS(self, root):
        result = 0
        referenceStack = [[root, 1]]

        while referenceStack:
            node, depth = referenceStack.pop()           

            if node:
                result = max(result, depth)
                referenceStack.append([node.left, depth+1])
                referenceStack.append([node.right, depth+1])
        
        return result

