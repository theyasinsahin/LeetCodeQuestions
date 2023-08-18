'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        return nums[n // 2]
        

        '''
        numbers = {}
        result = 0
        maxNumber = 0
        for num in nums:
            numbers[num] = 1 + numbers.get(num,0)
            if numbers[num] > maxNumber:
                result = num
            maxNumber = max(maxNumber, numbers[num])
        return result
        '''

        '''
        #Boyer Moore algorithm
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num
                
            if num == result:
                count += 1
            else:
                count -= 1
                
            count += 1 if num == result else -1
        return result
        '''
