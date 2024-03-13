# 풀이 참고함
# 딕셔너리: 존재성 확인하기
# 딕셔너리: 인덱스 저장하기
# 리스트: 값 저장하기
# 삭제 연산을 수행할 때, 가장 마지막 원소와 해당 원소를 뒤바꾼뒤, pop() 을 한다(!)
# 랜덤 선택의 경우, 원래 있는 함수를 사용한다! (random.choice(arr))

class RandomizedSet:

    def __init__(self):
        self.s = defaultdict(int)
        self.idx = dict()
        self.arr = []

    def insert(self, val: int) -> bool:
        if self.s[val]:
            return False
        self.s[val] += 1
        self.idx[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not self.s[val]:
            return False
        self.s[val] -= 1
        # last elem
        last = self.arr[-1]
        i = self.idx[val]
        self.idx[val], self.idx[last] = self.idx[last], self.idx[val]
        self.arr[-1], self.arr[i] = self.arr[i], self.arr[-1]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()