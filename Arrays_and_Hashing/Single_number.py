class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #base case 


        # for linear space and time we basically have to approach it using XOR operator that is XOR of two same numbers is 0
        if len(nums)==1:return nums[0]
        ans = 0 
        for i in range(len(nums)): 
            ans^=nums[i]
            print(ans)
        return ans ; 


        #basic idea is  - > for example 
        # [2,2,1] = XOR 0^2 = 2 , 2^2 = 0, 2^1 = 1
        #[4,1,2,1,2] = 0^4^1^2^1^2 = so here 2 and 2 cancels out and 1 and 1 cancels out too remains is 4 
        