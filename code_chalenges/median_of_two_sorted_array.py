"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        merged_array = nums1 + nums2
        sortedArray = self.quickSortArray(merged_array)        
        medianIndex = len(sortedArray)//2
        if len(sortedArray)%2 > 0:
            return merged_array[medianIndex]
        return (merged_array[medianIndex] + merged_array[medianIndex+1])/2

    def quickSortArray(self, input_array):
        if len(input_array)>0:
            pivote = input_array[0]
            small_numbers = [num for num in input_array[1:] if num <= pivote]
            large_numbers = [num for num in input_array[1:] if num > pivote]
            return self.quickSortArray(small_numbers) + [pivote] + self.quickSortArray(large_numbers)
        return []