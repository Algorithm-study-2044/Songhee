class Solution:
    def customSortString(self, order: str, str: str) -> str:
        priority ={key:index for index, key in enumerate(order)}
        a, b = [], []
        for char in str:
            if char in order:
                a.append(char)
            else:
                b.append(char)

        return ''.join(sorted(a, key=lambda x: priority[x])) + ''.join(b)