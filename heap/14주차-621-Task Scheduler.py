class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0] * 26
        for task in tasks:
            frequency[ord(task) - ord("A")] += 1
        max_frequency = max(frequency)
        return max((max_frequency - 1) * (n + 1) + frequency.count(max_frequency), len(tasks))