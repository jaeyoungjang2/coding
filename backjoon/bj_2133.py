cnt = int(input())
lst = [0]*31
lst[2] = 3
for i in range(3,31):
    if i%2==0 and i%4==0:
        lst[i] = (lst[i-2]*3)+1
    elif i%2==0:
        lst[i] = lst[i-2]*3

print(lst[cnt])

        
