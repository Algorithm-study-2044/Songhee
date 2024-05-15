class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = []
        if len(digits) ==0:
            return result

        def dfs(nums, index, dictionary, path, result):
            if index ==len(nums):
                result.append(path)
                return
            letters =dictionary[nums[index]]
            for letter in letters:
                dfs(nums, index+1, dictionary, path + letter, result)

        dfs(digits, 0, d, '', result)
        return result
    
    