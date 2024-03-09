class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p = [0 for _ in range(n)] # 
        o = [0 for _ in range(n)]
        for t in trust:
            p[t[1]-1] += 1
            o[t[0]-1] += 1
        
        trust = -1
        for i in range(len(p)):
            if p[i] == n-1:
                trust = i
                break

        if trust == -1:
            print('not everyone')
            return -1
        if o[trust]:
            print('outgoing edge', p, o, trust)
            return -1
        return trust+1