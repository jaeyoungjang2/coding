import sys
count = int(input())
lst = []
for i in range(count):
    temp_lst = []
    char = sys.stdin.readline().strip()
    for i in char:
        temp_lst.append(i)
    lst.append(temp_lst)
    
max_candy = 0

def check(lst):    
    global max_candy
    temp = 1
    init = lst[0]
    for i in lst[1:]:
        if init == i:
            temp += 1
        else:
            if max_candy < temp:
                max_candy = temp
            temp = 1
            init = i
    if max_candy < temp:
        max_candy = temp    


for i in range(count):
    for j in range(count-1):
        
        lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        check(lst[i])
        check(list(map(list,zip(*lst)))[j])
        check(list(map(list,zip(*lst)))[j+1])
        
        lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
#세로
for i in range(count):
    for j in range(count-1):
        lst[j][i], lst[j+1][i] = lst[j+1][i], lst[j][i]
        check(lst[j])
        check(lst[j+1])
        check(list(map(list,zip(*lst)))[i])
        lst[j][i], lst[j+1][i] = lst[j+1][i], lst[j][i]
        
print(max_candy)