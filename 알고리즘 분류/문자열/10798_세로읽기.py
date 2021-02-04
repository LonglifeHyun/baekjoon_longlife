board = [input() for _ in range(5)]
# print(board)

for i in range(15):
    for j in range(5):
        if len(board[j]) > i:
            print(board[j][i],end="")