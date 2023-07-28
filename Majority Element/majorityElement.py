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
