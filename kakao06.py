board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2],
         [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]

for lst in skill:
    type = lst[0]
    power = lst[5]

    for x in range(lst[1], lst[3]+1):
        for y in range(lst[2], lst[4]+1):
            if type == 1:
                board[x][y] -= power
            else:
                board[x][y] += power

answer = 0
for lst in board:
    for i in lst:
        if i > 0:
            answer += 1
print(answer)
print(board)
