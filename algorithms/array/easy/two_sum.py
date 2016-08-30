#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

#Example
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

#Update
The return format had been changed to zero-based indices. Please read the above updated description carefully.

#Complexity
Time: O(n)
"""


class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		num_to_index = {num: index for index, num in enumerate(nums)}
		for index, num in enumerate(nums):
			if target - num in num_to_index:
				if index != num_to_index[target - num]:
					return [index, num_to_index[target - num]] 
		"""
		Time: O(n^2)
		for i in range(len(nums)-1):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]
		"""

if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	solution = Solution()
	print solution.twoSum(nums, target)

