"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
class Solution(object):
    def removeDuplicates_sol1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        left_pointer = right_pointer = 0

        while right_pointer < len(nums):
            count = 1

            while (right_pointer + 1) < len(nums) and nums[right_pointer] == nums[right_pointer+1]:
                count += 1
                right_pointer += 1
            for i in range(min(2, count)):
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
            right_pointer += 1
        
        return left_pointer
      
    def removeDuplicates_sol2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        unqiue_num_count = 1
        forward_pointer = 1

        for i in range(1, n):
            if nums[i] == nums[i-1] and unqiue_num_count < 2:
               nums[forward_pointer] = nums[i]
               unqiue_num_count += 1
               forward_pointer += 1            
            elif nums[i] != nums[i-1]:
                nums[forward_pointer] = nums[i]
                forward_pointer += 1
                unqiue_num_count = 1
        return forward_pointer
