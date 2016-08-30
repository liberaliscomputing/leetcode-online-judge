#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

#Complexity
Time: O(n)
"""


class Solution(object):
	def containsNearbyDuplicate(self, nums, k):	
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""

		if len(nums) < 2:
			return False
		num_to_index = {}
		for i in range(len(nums)):
			if nums[i] in num_to_index:
				if i - num_to_index[nums[i]] <= k:
					return True
			num_to_index[nums[i]] = i
		return False

		"""
		Time: O(n^2)
		for i in range(len(nums)-1):
			for j in range(i+1, len(nums)):
				if (nums[i] == nums[j]) and (j - i <= k):
					return True
		return False
		"""

if __name__ == '__main__':
	nums = [1, 0, 1, 1]
	k = 1
	solution = Solution()
	print solution.containsNearbyDuplicate(nums, k)

