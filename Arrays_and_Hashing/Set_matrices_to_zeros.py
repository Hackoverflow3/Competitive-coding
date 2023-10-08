from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        chk_R,chk_C= set(), set()
        C,R = len(matrix),len(matrix[0])
        for i in range(C):
            for j in range(R):
                if matrix[i][j]==0:
                    chk_R.add(i)
                    chk_C.add(j)
        for i in chk_R:
            for j in range(0,R):
                matrix[i][j]=0
        print(chk_C)
        for i in chk_C:
            for j in range(0,C):
                matrix[j][i]=0
        

