"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
      4
     /\
    2  7
  /\   /\
 1  3 6  9

Input: root = [4,2,7,1,3,6,9]

Output: [4,7,2,9,6,3,1]
      4
     /\
    7  2
  /\   /\
 9  6 3  1

"""

# Time complexity analysis - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dfs(root)
        return root

def dfs(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp

        dfs(root.left)
        dfs(root.right)