#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

#Example 19 is a happy number
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

#Complexity
Time: O(logn)
"""


class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		recur = []
		while True:
			stringfy = list(str(n))
			sum_of_square = 0
			for s in stringfy:
				sum_of_square += int(s) ** 2
			if sum_of_square == 1:
				return True
			if sum_of_square in recur:
				return False
			recur.append(sum_of_square)
			n = sum_of_square

if __name__ == '__main__':
	n = 19
	solution = Solution()
	print solution.isHappy(n)
	
