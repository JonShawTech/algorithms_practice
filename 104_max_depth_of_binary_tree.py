"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

"""
# Time complexity analysis - O(n), n = nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        depth = []
        dfs(root,depth,0)

        return max(depth)
         
def dfs(root,depth,count):

    if root is not None:
        count += 1       
        dfs(root.left,depth,count)
        depth.append(count)        
        dfs(root.right,depth,count)
        