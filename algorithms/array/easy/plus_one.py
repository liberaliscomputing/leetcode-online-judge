#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

#Complexity
Time: O(n)
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        if carry:
            digits.insert(0, carry)
        return digits
                
        """
        #Solution with strinfy digits
        stringfy = ''.join([str(d) for d in digits])
        digify = int(stringfy) + 1
        stringfy = list(str(digify))
        return [int(d) for d in stringfy]
        """

if __name__ == '__main__':
	digits = [9, 0, 0, 9]
	solution = Solution()
	solution.plusOne(digits)
	print digits

