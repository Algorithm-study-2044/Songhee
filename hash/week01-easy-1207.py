from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr2 = Counter(arr)
        arr3 = []
        for a in arr2:
            arr3.append(arr2[a])
        print(arr3)
        return len(set(arr3)) == len(arr3)