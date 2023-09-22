"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s.lower():
            if (ascii(char)< ascii("a") or ascii(char)> ascii('z') or char == " ") and not char.isdigit():
                s=s.replace(char, "")
        left=0
        right=len(s) - 1
        while left<right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        for char in s.lower():
            if not char.isalnum():
                s = s.replace(char, "")        
        return True if s == s[::-1] else False