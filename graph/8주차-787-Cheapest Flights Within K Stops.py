class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        d = defaultdict(list)
        for flight in flights:
            f = flight[0]
            t = flight[1]
            w = flight[2]
            d[f].append([t, w])
        
        h = []
        dp = [[float('inf') for stop in range(k+2)] for node in range(n)]
        heapq.heappush(h, (0, 0, src)) # cost, stop, node
        while h:
            curr_cost, curr_stop_cnt, curr_node = heapq.heappop(h)
            if curr_stop_cnt > k:
                continue
            next_stop_cnt = curr_stop_cnt + 1
            for (next_node, cost) in d[curr_node]:
                next_cost = curr_cost + cost
                if dp[next_node][next_stop_cnt] > next_cost:
                    dp[next_node][next_stop_cnt] = next_cost
                    heapq.heappush(h, (next_cost, next_stop_cnt, next_node))

        ans = min(dp[dst])
        if ans == float('inf'):
            return -1
        return ans
        