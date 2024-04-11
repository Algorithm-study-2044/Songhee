class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # face-up: 현재 파워가 최소한 tokens[i] 이상이면 tokens[i] 만큼 파워 깎고 score +1
        # face-down: 현재 점수가 최소한 1점 이상일 때, 점수를 깎고 tokens[i] 파워를 얻고 1점 잃음

        # 그리디하게 푸는 방식?
        # Greedy: Buy tokens with small values, 
        #         Sell tokens with large values to increase power!

        tokens.sort()
        score = 0
        i, j = 0, len(tokens)-1
        for _ in tokens:
            # face-up
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
            # face-down
            elif score:
                power += tokens[j]
                j -= 1
                score -= 1
                if j<i:
                    score += 1
                    break
            else:
                break
        
        
        return score
        