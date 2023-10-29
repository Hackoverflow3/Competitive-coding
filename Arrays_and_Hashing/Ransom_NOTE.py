class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if magazine.count(ransomNote[i])<ransomNote.count(ransomNote[i]):
                return False;
        return True;