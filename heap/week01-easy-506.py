class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = [(i, score[i]) for i in range(len(score))]
        arr.sort(key=lambda x: -x[1])
        ans = []
        for rank in range(1, len(score)+1):
            if rank == 1: r = 'Gold Medal'
            elif rank == 2: r = 'Silver Medal'
            elif rank == 3: r = 'Bronze Medal'
            else: r = f'{rank}'
            ans.append((arr[rank-1][0], r))
        ans.sort(key=lambda x: x[0])
        print(ans)
        return [a[1] for a in ans]

            