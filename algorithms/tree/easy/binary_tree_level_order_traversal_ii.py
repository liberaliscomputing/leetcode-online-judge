"""
#Description
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

#Complexity
Time: O(n) 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		traversal = []
		if not root:
			return traversal
		current = [root]
		while current:
			nodes = []
			leaves = []
			for node in current:
				nodes.append(node.val)
				if node.left:
					leaves.append(node.left)
				if node.right:
					leaves.append(node.right)
			traversal.append(nodes)
			current = leaves
		return traversal[::-1]

