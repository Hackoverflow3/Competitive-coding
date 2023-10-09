class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        left,right,ans= 0,N-1,''
        while left<=right:
            mid = left + (right - left)//2
            if ord(letters[mid])<=ord(target):
                left = mid + 1 
            if ord(letters[mid])>ord(target):
                ans = letters[mid]
                right = mid -1
        if ans  =='':
            return letters[0]
        return ans ; 
        