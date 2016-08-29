#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

#Note
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

#Complexity
Time: O(n)
"""


class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		k = k % len(nums)
		for i in range(k):
			nums.insert(0, nums[-1])
			del nums[-1]

if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5, 6, 7]
	k = 3
	solution = Solution()
	solution.rotate(nums, k)
	print nums

