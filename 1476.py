import sys
E, S, M = 0, 0, 0
year = 0
lst = list(map(int,sys.stdin.readline().split()))
while True:
    if E == lst[0] and S == lst[1] and M == lst[2]:
        break
    else:
        E += 1
        S += 1
        M += 1
        year += 1
        if E > 15:
            E = 1
        if S > 28:
            S = 1
        if M > 19:
            M = 1
print(year)