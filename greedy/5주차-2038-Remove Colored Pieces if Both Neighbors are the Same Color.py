class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = colors.split('B')
        acnt = 0
        for aa in a:
            acnt += max(len(aa)-2, 0)
            
        a = colors.split('A')
        bcnt = 0
        for aa in a:
            bcnt += max(len(aa)-2, 0)
        
        return True if acnt > bcnt else False

    # 다른 사람 풀이
    def winnerOfGame2(self, colors: str) -> bool:
        a_points = 0
        b_points = 0
        for i in range(1,len(colors)-1):
            if colors[i-1] == colors[i] and colors[i+1] == colors[i]:
                if colors[i]=="A":
                    a_points += 1
                else:
                    b_points += 1
        
        return True if a_points > b_points else False