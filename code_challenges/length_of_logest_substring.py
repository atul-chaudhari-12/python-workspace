# Challange 1
"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters. 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_len = len(s)
        if string_len in [0,1]:
            return string_len
        substring_set = {s[0]}
        max_length = 0
        length = 1
        i=0
        while i < string_len:
            if (s[i]!=s[i-1] and s[i] not in substring_set):
                substring_set.add(s[i])
                length = length + 1
                i += 1
                if(max_length<length):
                    max_length = length
            else:
                if (length==1):
                    i += 1
                else:
                    substring_set.clear()
                    i = i - length + 1
                    length = 0
        return max(max_length, length)    


# Challenge 2
"""
Given a string you need to print longest possible substring that has exactly M unique characters. 
If there is more than one substring of longest possible length, then print any one of them.

Examples: 
    Input: Str = “aabbcc”, k = 1
    Output: 2
    Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.

    Input: Str = “aabbcc”, k = 2
    Output: 4
    Explanation: Max substring can be any one from {“aabb” , “bbcc”}.

    Input: Str = “aabbcc”, k = 3
    Output: 6
    Explanation: 
    There are substrings with exactly 3 unique characters
    {“aabbcc” , “abbcc” , “aabbc” , “abbc” }
    Max is “aabbcc” with length 6.

    Input: Str = “aaabbb”, k = 3
    Output: Not enough unique characters
    Explanation: There are only two unique characters, thus show error message. 
"""
class Solution(object):
    def lengthOfLongestSubstringWithKUniqueCharacters(s, k):
        start_index = 0
        end_index = 0
        string_length = len(s)
        maximum_length = 0        
        hash_map = {}
        while (end_index < string_length):            
            if not hash_map.get(s[end_index]):                
                k -= 1

            hash_map[s[end_index]] = end_index

            while k < 0:
                if hash_map.get(s[start_index], -2) == start_index:
                    k += 1
                    del hash_map[s[start_index]]
                start_index += 1

            maximum_length = max(maximum_length, end_index-start_index+1)
            end_index += 1
        
        return maximum_length


                    