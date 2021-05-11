
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
answer = []
p_lst = []
x_lst = []


for place in places:
    temp = 1
    bool = True
    # place = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
    # lst = [['P', 'O', 'O', 'O', 'P'], ['O', 'X', 'P', 'O', 'O'], ['O', 'X', 'X', 'X', 'X'], ['O', 'O', 'P', 'O', 'X'], ['P', 'X', 'X', 'X', 'P']]
    target_lst = ['PP', 'POP', 'POOP', 'POOP']
    lst = list(map(list, zip(*place)))
    reverse_lst = list(map(list, zip(*lst)))
    while bool:
        for i in range(5):
            reverse_string = ''.join(reverse_lst[i])
            forward_string = ''.join(lst[i])
            for j in target_lst:
                if j in forward_string:
                    # print(forward_string)
                    temp = 0
                    bool = False
                    break
                elif j in reverse_string:
                    temp = 0
                    bool = False
                    break
        for row in range(0, 4):
            for col in range(0, 5):
                if col == 0:
                    if lst[row][0] == 'P' and lst[row+1][1] == 'P' and (lst[row][1] != 'X' and lst[row+1][0] != 'X'):
                        temp = 0
                        bool = False
                        break
                elif col == 4:
                    if lst[row][4] == 'P' and lst[row+1][3] == 'P' and (lst[row][3] != 'X' and lst[row+1][4] != 'X'):
                        temp = 0
                        bool = False
                        break
                else:
                    if lst[row][col] == 'P':
                        if lst[row+1][col-1] == 'P' and (lst[row+1][col] != 'X' and lst[row][col-1] != 'X'):
                            temp = 0
                            bool = False
                            break
                        elif lst[row+1][col+1] == 'P' and (lst[row+1][col] != 'X' and lst[row][col+1] != 'X'):
                            temp = 0
                            bool = False
                            break
        bool = False
    answer.append(temp)
print(answer)
