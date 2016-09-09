#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

#Note
You may assume the string contains only lowercase alphabets.

#Follow up
What if the inputs contain unicode characters? How would you adapt your solution to such case?

#Complexity
Time: O(n)
Space: O(n)
"""

from collections import Counter


class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) != len(t):
			return False
		ds = Counter(list(s))
		dt = Counter(list(t))
		return (ds == dt) == True

		"""
		if len(s) != len(t):
			return False
		ds = Counter(list(s))
		for char in t:
			if char in ds:
				if ds[char] < 1:
					return False
				ds[char] -= 1
			else:
				return False
		return True
		"""
		"""
		if len(s) != len(t):
			return False
		ds = Counter(list(s))
		dt = Counter(list(t))
		for k in ds.keys():
			if k in dt:
				if ds[k] != dt[k]:
					return False
			else:
				return False
		return True
		"""

if __name__ == '__main__':
	s = 'anagram' 
	t = 'nagaram'
	solution = Solution()
	print solution.isAnagram(s, t)

