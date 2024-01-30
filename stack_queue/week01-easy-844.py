from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = deque()
        tt = deque()
        for sss in s:
            ss.append(sss)
            if sss == '#':
                ss.pop()
                if ss: ss.pop()
        for ttt in t:
            tt.append(ttt)
            if ttt == '#':
                tt.pop()
                if tt: tt.pop()
        s1 = ''.join(ss) 
        t1 = ''.join(tt)
        print(s1, t1)
        return s1 == t1
        