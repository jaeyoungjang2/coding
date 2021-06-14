num = int(input())

count = 0
res = 0
while True:
    if num < pow(10, count+1)-1:
        break
    res += (9*pow(10, count)) * (count+1)
    count += 1


res += (num - pow(10, count)+1) * (count+1)
print(res)
