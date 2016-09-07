#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given two arrays, write a function to compute their intersection.

#Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

$Note
Each element in the result must be unique.
The result can be in any order.

#Complexity
Time: O(n^2)
Space: O(n)
"""


class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		results = []
		for num1 in nums1:
			for num2 in nums2:
				if (num1 == num2) and (num1 not in results):
					results.append(num1)
		return results

		"""
		#With set()
		set1 = set(nums1)
		set2 = set(nums2)
		return list(set1.intersection(set2))
		"""

if __name__ == '__main__':
	nums1 = [1, 2, 2, 1]
	nums2 = [2, 2]
	solution = Solution()
	print solution.intersection(nums1, nums2) == [2]

