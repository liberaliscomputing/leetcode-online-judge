#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

#Complexity
Time: O(n)
"""


class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""

		#One pass
		if len(nums) < 1:
			return False
		num_to_cnt = {}
		for num in nums:
			if num in num_to_cnt:
				return True
			num_to_cnt[num] = 1
		return False

		"""
		if len(nums) < 1:
			return False
		num_to_cnt = {}
		for num in nums:
			num_to_cnt[num] = num_to_cnt.get(num, 0) + 1
		for n, c in num_to_cnt.items():
			if c > 1:
				return True
		return False
		"""

if __name__ == '__main__':
	nums = [1, 0, 1, 1]
	solution = Solution()
	print solution.containsDuplicate(nums)
