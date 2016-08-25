#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#Note
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

#Complexity
Time: O(n*logn)
"""


class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""

		merged_index = m + n - 1
		m -= 1
		n -= 1
		while m >= 0 and n >= 0:
			if nums1[m] > nums2[n]:
				nums1[merged_index] = nums1[m]
				m -= 1
			else:
				nums1[merged_index] = nums2[n]
				n -= 1
			merged_index -= 1
		if m < 0:
			nums1[:n+1] = nums2[:n+1]
				
		"""
		#Solution with the sort method
		for i in range(n):
			nums1[i+m] = nums2[i]
		nums1.sort()
		"""

if __name__ == '__main__':
	nums1, m, nums2, n = [1, 2, 3, 4, 0, 0, 0, 0], 4, [1, 2, 3, 4], 4
	solution = Solution()
	solution.merge(nums1, m, nums2, n) 
	print nums1

