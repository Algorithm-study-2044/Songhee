# 풀이 참고, 다시 풀기

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        strset = set(s)
        stack = []
        count = Counter(s)
        for ch in s:
            count[ch] -= 1
            if ch in stack:
                continue
            # 스택에 넣기 전에 
            # 현재 문자가 앞에 쌓인 문자보다 사전식으로 앞선다면 
            # 앞에 쌓인 문자가 뒤에도 있는지 확인
            # 뒤에도 있다면 쌓인 문자를 빼고 없다면 그대로 두고 현재 문자를 삽입한다.
            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)

        return ''.join(stack)