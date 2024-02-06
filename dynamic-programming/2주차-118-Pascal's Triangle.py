class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        ans = [[1], [1,1]]
        for n in range(3, numRows+1):
            ref = ans[-1]
            tmp = [1]
            for i in range(len(ref)-1):
                tmp.append(ref[i]+ref[i+1])
            ans.append(tmp+[1])
        return ans