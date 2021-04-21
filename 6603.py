import sys, itertools
while True:
    lst = list(map(int,sys.stdin.readline().strip().split()))
    count = lst[0]
    lst = lst[1:]
    if count == 0:
        break
    else:
        pool = ['0']*6+['1']*(count-6)
        boolst = (set(map(''.join, itertools.permutations(pool))))
        # print(set(boolst))
        for case in sorted(boolst):
            for index, i in enumerate(case):
                if i == '0':
                    print(lst[index], end=' ')
            print()
        print()


        
        
    