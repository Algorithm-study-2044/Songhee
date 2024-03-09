class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0]
        b = edges[1]
        for aa in a:
            for bb in b:
                if aa == bb:
                    return aa
        return 0