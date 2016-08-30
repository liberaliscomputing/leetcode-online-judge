#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

#Example
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

#Complexity
Time: O(n)
"""


class Solution(object):
	def removeDuplicates(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
		if len(nums) < 1:
			return 0
		index = 1
		start = 0
		for i in range(1, len(nums)):
			if nums[i] != nums[start]:
				nums[index] = nums[i]
				index += 1
				start += 1
		return index

if __name__ == '__main__':
	nums = [1, 1, 1, 2, 2, 3]
	solution = Solution()
	unique = solution.removeDuplicates(nums)
	print nums, unique

