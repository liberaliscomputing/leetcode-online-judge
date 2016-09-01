#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

#Complexity
Time: O(n^2)
"""


class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""

		if numRows == 0:
			return []
		triangle = [[1]]
		for i in range(1, numRows):
			triangle.append([1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1])-1)] + [1])
		return triangle

		"""
		if numRows == 0:
			return []
		triangle = []
		for i in range(numRows):
			if i == 0:
				triangle.append([1])
			elif i == 1:
				triangle.append([1, 1])
			else:
				triangle.append([1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1])-1)] + [1])
		return triangle
		"""
		"""
		#With zip()
		if numRows == 0:
			return []
		triangle = [[1]]
		for i in range(1, numRows):
			triangle.append([1] + [sum(pair) for pair in zip(triangle[i-1][0:i-1], triangle[i-1][1:])] + [1])
		return triangle
		"""

if __name__ == '__main__':
	numRows = 7
	solution = Solution()
	print solution.generate(numRows)

