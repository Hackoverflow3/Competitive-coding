class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            
        def check(arr,st,T):
    
            count = 0 
            for i in arr:
                if i[T]==st:count+=1
            if count==len(arr):
                return True;
            return False;

        ans = ""
        k_small,search= 9223372036854775807,""
        for i in range(len(strs)):
            if len(strs[i])<k_small:
                search = strs[i]
                k_small = len(strs[i])
        ll = 0 
        for i in range(len(search)):
            if check(strs,search[i],i) and ll==i:
                ans+=search[i]
                ll+=1
        return ans;