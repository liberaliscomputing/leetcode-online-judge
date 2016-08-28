#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

#Complexity
Time: O(n)
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Solution with hash table
        elements = {}
        for i in nums:
            elements[i] = elements.get(i, 0) + 1
        for (k, v) in elements.items():
            if v > len(nums) / 2:
                return k

if __name__ == '__main__':
	nums = [1, 2, 2, 3, 3, 3, 3, 3]
	solution = Solution()
	print solution.majorityElement(nums)

