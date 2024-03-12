class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cnts = [0 for a in range(amount+1)]

        for a in range(1, amount+1):
            arr = [cnts[a-c] for c in coins if a-c >= 0 and cnts[a-c]!=-1 ]
            if not arr:
                cnts[a] = -1
                continue
            min_cnt = min(arr)
            cnts[a] = 1+min_cnt
            # print(a, cnts)
            
        return cnts[amount]