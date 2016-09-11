#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

#Examples
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

#Notes
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

#Complexity
Time: O(n)
"""


class Solution(object):
	def wordPattern(self, pattern, string):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		if len(pattern) != len(string.split()):
			return False
		dic = {}
		for p, s in zip(list(pattern), string.split()):
			if p in dic:
				if dic[p] != s:
					return False
			else:
				if s in dic.values():
					return False
			dic[p] = s
		return True

if __name__ == '__main__':
	pattern = 'abba'
	string = 'dog cat cat dog'
	solution = Solution()
	print solution.wordPattern(pattern, string)

