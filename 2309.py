import sys
total_height = 0
lst = []
for i in range(9):
    height = int(sys.stdin.readline())
    total_height += height
    lst.append(height)

for i in range(8):
    for j in range(i+1,9):
        print(i , j)
        if (total_height - (lst[i] + lst[j])) == 100 :
            human1 = lst[i]
            human2 = lst[j]

del lst[lst.index(human1)]
del lst[lst.index(human2)]

lst = sorted(lst)
for i in lst:
    print(i)



