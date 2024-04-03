class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0]*n
        stack = []
        task, action, time = logs[0].split(':')

        task = int(task)
        time = int(time)
        stack.append(task)

        for i in range(1,len(logs)):
            prev_time = time
            prev_action = action
            task, action, time = logs[i].split(':')
            task = int(task)
            time = int(time)

            if action == 'start':
                if len(stack) != 0:
                    if prev_action == 'start':
                        res[stack[-1]] += (time - prev_time)
                    elif prev_action == 'end':
                        res[stack[-1]] += (time - prev_time-1)
                stack.append(task)
            else:
                if prev_action == 'start':
                    res[stack[-1]] += (time - prev_time + 1)
                elif prev_action == 'end':
                    res[stack[-1]] += (time - prev_time)
                stack.pop()

        return res
