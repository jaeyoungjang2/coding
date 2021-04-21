import sys, itertools

dic = {}
count = int(input())
for i in range(count):
    lst = list(map(int,sys.stdin.readline().strip().split()))
    for index, j in enumerate(lst):
        try:
            dic[i][index] = j
        except:            
            dic[i] = {}
            dic[i][index] = j

def cal(case,dic):
    if case[0] != '0':
        
        return 0
    temp = 0
    case += case[0]
    
    for i in range(len(case)-1):
        if dic[int(case[i])][int(case[i+1])]:
            temp += dic[int(case[i])][int(case[i+1])]
        else:
            return 0
    return temp

def main(count,dic):
    result = 10000000000000000
    pool = []
    for i in range(count):
        pool.append(str(i))    
    
    comb = list(map(''.join, itertools.permutations(pool)))
    
    for i in comb:
        temp = cal(i,dic)
        if temp != 0 and temp < result:
            result = temp
    print(result)    
    
                



main(count, dic)