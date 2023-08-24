"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening_brackets = ["{", "[", "("]
        closing_brackets = ["}", ")", "]"]
        relation_dict = {"{": "}", "[":"]", "(":")"}
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char in closing_brackets:
                    stacked_char = stack.pop
                    if relation_dict[stacked_char] != char:
                        return False
                    
        if stack:
            return False
        return True