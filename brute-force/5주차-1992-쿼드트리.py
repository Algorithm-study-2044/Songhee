def compress(board):
    s = sum([sum(b) for b in board])
    if s == len(board)*len(board):
        return '1'
    if s == 0:
        return '0'
    n = len(board)//2
    a = compress([[board[i][j] for j in range(n)] for i in range(n)])
    b = compress([[board[i][j] for j in range(n, 2*n)] for i in range(n)])  
    c = compress([[board[i][j] for j in range(n)] for i in range(n, 2*n)])
    d = compress([[board[i][j] for j in range(n, 2*n)] for i in range(n, 2*n)])
    return f'({a}{b}{c}{d})'

n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]

print(compress(board))