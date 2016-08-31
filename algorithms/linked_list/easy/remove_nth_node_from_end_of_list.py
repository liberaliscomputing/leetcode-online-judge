#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description:
Given a linked list, remove the nth node from the end of list and return its head.
For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

#Note
Given n will always be valid.
Try to do this in one pass.

#Complexity
Time: O(n)
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def get_node(self):
		print self.val
		if self.next:
			self.next.get_node()


class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		if not head:
			return head
		dummy = ListNode(-1)
		dummy.next = head
		fast = slow = dummy
		while fast and (n >= 0):
			fast = fast.next
			n -= 1
		while fast:
			fast = fast.next
			slow = slow.next
		slow.next = slow.next.next
		return dummy.next

if __name__ == '__main__':
	n5 = ListNode(5)
	n4 = ListNode(4)
	n3 = ListNode(3)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n = 2
	solution = Solution()
	result = solution.removeNthFromEnd(n1, n)
	result.get_node()

