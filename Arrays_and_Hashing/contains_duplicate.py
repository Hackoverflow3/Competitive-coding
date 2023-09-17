class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True;
        return False; 




#best solution for this would be to use a set that would check if the value is present in that or not 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Hashset = set()
        nums.sort()
        for i in range(len(nums)):
            if i in Hashset:
                return True;
            Hashset.add(i)
        return False; 


