#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array of integers, every element appears twice except for one. Find that single one.

#Note
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Complexity
Time: O(n)
"""


class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums_to_dic = {}
		for num in nums:
			nums_to_dic[num] = nums_to_dic.get(num, 0) + 1
		for num, frq in nums_to_dic.items():
			if frq == 1:
				return num

if __name__ == '__main__':
	nums = [1, 2, 3, 4, 3, 2, 1]
	solution = Solution()
	print solution.singleNumber(nums)
	
