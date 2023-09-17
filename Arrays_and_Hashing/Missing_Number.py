class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0 ; 
        for i in range(len(nums)-1):
            if nums[i]+1!=nums[i+1]:
                return nums[i]+1;
        return nums[len(nums)-1]+1;

        # best solution its basically like sum of all numbers from 0-n - sum(array)
        rs = len(nums)
        for i in range(len(nums)):
            rs+=(i-nums[i])
        return rs; 