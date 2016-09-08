#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given two arrays, write a function to compute their intersection.

#Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

#Note
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

#Follow up
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

#Complexity
Time: O(n)
Space: O(n)
"""

from collections import Counter


class Solution(object):
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""

		#Follow-up 1
		nums1 = sorted(nums1)
		nums2 = sorted(nums2)
		m = n = 0
		results = []
		while m < len(nums1) and n < len(nums2):
			if nums1[m] == nums2[n]:
				results.append(nums1[m])
				m += 1
				n += 1
			elif nums1[m] > nums2[n]:
				n += 1
			else:
				m +=1
		return results

		"""
		#Follow-up 2
		dic1 = {}
		for num1 in nums1:
			dic1[num1] = dic1.get(num1, 0) + 1
		dic2 = {}
		for num2 in nums2:
			dic2[num2] = dic2.get(num2, 0) + 1
		if len(dic1.keys()) > len(dic2.keys()):
			dic1, dic2 = dic2, dic1
		results = []
		for k in dic1:
			if k in dic2:
				for i in range(min(dic1[k], dic2[k])):
					results.append(k)
		return results
		"""
		
		"""
		#Follow-up 3
		dic1 = {}
		for num1 in nums1:
			dic1[num1] = dic1.get(num1, 0) + 1
		results = []
		for num2 in nums2:
			if num2 in dic1 and dic1[num2] != 0:
				results.append(num2)
				dic1[num2] -= 1
		return results
    """

if __name__ == '__main__':
	nums1 = [1, 2, 2, 1]
	nums2 = [2, 2]
	solution = Solution()
	print solution.intersect(nums1, nums2)
