#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

#Complexity
Time: O(n^2)
"""


class Solution(object):
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		if rowIndex < 0:
			return None
		triangle = [1]
		for i in range(1, rowIndex+1):
			triangle = [1] + [sum(pair) for pair in zip(triangle[0:i-1], triangle[1:])] + [1]
		return triangle

if __name__ == '__main__':
	rowIndex = 3
	solution = Solution()
	print solution.getRow(rowIndex)
	