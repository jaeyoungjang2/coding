def find_guy(lst,target):
    for i in range(9):
        for j in range(i+1,9):
            if lst[i]+lst[j] == target:
                return(i,j)
lst = []

for i in range(9):
    lst.append(int(input()))
lst = sorted(lst)
length = sum(lst)
target = length - 100
except_1, except_2 = find_guy(lst,target)

for i in lst:
    if i == lst[except_1] or i == lst[except_2]:
        continue
    else:
        print(i)