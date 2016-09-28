#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given a singly linked list, determine if it is a palindrome.

#Follow up:
Could you do it in O(n) time and O(1) space?

#Complexity
Time: O(n)
Space: O(1)
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head:
			return True
		dummy = ListNode(-1)
		dummy.next = head
		slow = fast = dummy
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		curr = slow.next
		last = None
		while curr:
			next = curr.next
			curr.next = last
			last, curr = curr, next
		while last:
			if last.val == head.val:
				last = last.next
				head = head.next
			else:
				return False
		return True

if __name__ == '__main__':
	n5 = ListNode(1)
	n4 = ListNode(2)
	n3 = ListNode(3)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	solution = Solution()
	print solution.isPalindrome(n1) == True

