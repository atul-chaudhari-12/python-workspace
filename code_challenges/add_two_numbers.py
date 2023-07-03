"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbersOne(self, l1, l2):
        dummy_node = ListNode(0)
        current_node = dummy_node
        carry = 0

        while l1 or l2 or carry:
            number_sum = carry

            if l1:
                number_sum += l1.val
                l1 = l1.next
            
            if l2:
                number_sum += l2.val
                l2=l2.next
            
            carry = number_sum // 10
            current_node.next = ListNode(number_sum%10)
            current_node = current_node.next
            
        return dummy_node.next

    def addTwoNumbersTwo(self, l1, l2):
        head1 = l1
        head2 = l2
        number1 = number2 = 0
        multiplier = 1
        while head1 or head2:
            number1 = number1 + (head1.val * multiplier if head1 else 0)
            number2 = number2 + (head2.val * multiplier if head2 else 0)
            multiplier = multiplier * 10
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        
        addition = number1 + number2
        dummy = ListNode(0)        
        current_node = dummy
        while addition > -1:
            temp_number = addition % 10
            addition = addition // 10            
            current_node.next = ListNode(temp_number)                
            current_node = current_node.next
            if addition == 0:
                break
        return dummy.next