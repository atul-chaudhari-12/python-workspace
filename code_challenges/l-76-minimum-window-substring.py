"""Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left_pointer = 0
        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char,0)
        
        have, need = 0, len(countT)
        result_pointers, results_len = [-1,-1], float('inf')

        for right_pointer in range(len(s)):
            window[s[right_pointer]] = 1 + window.get(s[right_pointer], 0)

            if s[right_pointer] in countT and window[s[right_pointer]] == countT[s[right_pointer]]:
                have += 1
            
            while have == need:
                if (right_pointer-left_pointer+1) < results_len:
                    results_len = right_pointer-left_pointer+1
                    result_pointers = [left_pointer, right_pointer]
                window[s[left_pointer]] -= 1
                if s[left_pointer] in countT and window[s[left_pointer]] < countT[s[left_pointer]]:
                    have -= 1
                left_pointer += 1

        return s[result_pointers[0]:result_pointers[1]+1] if results_len != float('inf') else ""
