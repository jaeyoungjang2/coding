text = input().split()
count = int(input())
lst = []
temp = []
for i in text:
    lst.append(i)
  
for i in range(count):
    cmd = input().split()
    if cmd[0] == 'L' or cmd[0] == 'B':
        if len(lst) != 0:
            temp.append(lst.pop())
    elif cmd[0] == 'D':
        if len(temp) != 0:
            lst.append(temp.pop())
    else:
        lst.append(cmd[1])

print(''.join(lst)+''.join(temp))