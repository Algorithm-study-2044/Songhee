class Solution:
    index = []
    weights = []

    def __init__(self, w: List[int]):
        s = sum(w)
        self.weights = [ww/s for ww in w]
        self.index = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.index, self.weights)[0]


# binary search 관련 풀이
import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        S = sum(w)
        probs = [weight / S for weight in w]
        self.ranges = probs
        for i in range(1, len(probs)):
            self.ranges[i] = self.ranges[i-1] + self.ranges[i] # 누적함수 만들어서

    def pickIndex(self) -> int:
        r = random.random()
        return bisect.bisect(self.ranges, r) # 사이에 낀 인덱스 찾기