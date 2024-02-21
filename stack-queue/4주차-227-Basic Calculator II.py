class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+': stack.append(num)
            if op == '-': stack.append(-num)
            if op == '*': stack.append(stack.pop() * num)
            if op == '/': stack.append(int(stack.pop() / num))
        s = s.replace(' ', '')
        stack = []
        num = 0
        pre_op = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif s[i] in '+-*/':
                update(pre_op, num)
                num = 0
                pre_op = s[i]
        update(pre_op, num)
        return sum(stack)