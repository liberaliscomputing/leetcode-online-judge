#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

#Note
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

#Complexity
Time: O(n)
"""


class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 1:
        return False
    carry = 0
    for i in range(len(nums)):
        if nums[i] != 0:
           nums[carry], nums[i] = nums[i], nums[carry]
           carry += 1

if __name__ == '__main__':
	nums = [0, 1, 0, 3, 12]
	solution = Solution()
	solution.moveZeroes(nums)
	print nums
