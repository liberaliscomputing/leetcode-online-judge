#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

#Note
You may assume both s and t have the same length.

#Complexity
Time: O(n^2)
Space: O(n)
"""


class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		s_to_t = {}
		for c_of_s, c_of_t in zip(s, t):
			if s_to_t.get(c_of_s):
				if s_to_t[c_of_s] != c_of_t:
					return False
			else:
				if c_of_t in s_to_t.values():
					return False
			s_to_t[c_of_s] = c_of_t
		return True

if __name__ == '__main__':
	s = 'egg'
	t = 'add'
	solution = Solution()
	print solution.isIsomorphic(s, t)
	
