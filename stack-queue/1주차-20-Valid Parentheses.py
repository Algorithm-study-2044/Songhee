from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        try:
            for ss in s:
                print(ss)
                if ss == '(':
                    stack.append('(')
                elif ss == ')':
                    tmp = stack.pop()
                    if tmp != '(':
                        return False

                elif ss == '{':
                    stack.append('{')
                elif ss == '}':
                    tmp = stack.pop()
                    if tmp != '{':
                        return False
                    
                elif ss == '[':
                    stack.append('[')
                elif ss == ']':
                    tmp = stack.pop()
                    if tmp != '[':
                        return False
        except:
            return False
        return len(stack) == 0