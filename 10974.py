import sys

n = int(input())
result = []
# 리스트에서 제일 마지막 값을 뽑는다.
def permutation(lst):
    temp = []
    standard = lst[-1]-1
    while lst:        
        i = lst.pop()                
        if standard < i:
            standard = i
            temp.append(i)            
        else:
            lst.append(i)
            
            # temp에 들어있는 것 중 last 값보다는 큰 수중 가장 작은 수를 찾는다.
            # temp에 들어있는 수는 오름차순
            last = lst[-1]            
            for lc, i in enumerate(temp):                
                if last < i:
                    lst[-1], temp[lc] = i, last
                    break
            for i in temp:
                lst.append(i)            
            return(lst)
    return -1

for i in range(1,n+1):
    result.append(i)
print(result)
while True:
    if result == -1:
        break
    else:
        for i in result:
            print(i, end=' ')
        print()
    result = permutation(result)