#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum value of F(0), F(1), ..., F(n-1).

#Note
n is guaranteed to be less than 10^5.

#Example
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

#Complexity
Time: O(n)
"""


class Solution(object):
	def maxRotateFunction(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		n = len(A)
		if n < 1:
			return 0
		sumA = sum(A)
		sumN = sum(id * num for id, num in enumerate(A))
		results = [sumN]
		for i in range(1, n):
			sumN += sumA - n * A[n-i]
		results.append(sumN)
		return max(results)

		"""
		Time exceeded error
		n = len(A)
		if n < 1:
		return 0
		results = []
		for k in range(n):
		sum = 0
		B = A
		if k != 0:
		B = A[-k:] + A[0:n-k]
		for id, num in enumerate(B):
		sum += id * num
		results.append(sum)
		return max(results)
		"""

if __name__ == '__main__':
	nums = [4, 3, 2, 6]
	solution = Solution()
	print 26 == solution.maxRotateFunction(nums)

