def transfer(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def isPrime(n):
    if (n < 2):
        return False

    for i in range(2, n + 1):
        if i * i <= n:
            if n % i == 0:
                return False
        else:
            return True


n = "437674"
k = "3"
answer = 0
n = transfer(int(n), int(k))

n = str(n)
string = n[0]
problem = n[0]
for i in n[1:]:
    print(i)
    if string == "0" and i == "0":
        continue
    else:
        string = i
        problem += i

if problem[-1] == "0":
    problem += "1"

problem = "10" + problem
primeLst = problem.split("0")

for candidate in primeLst:
    if isPrime(int(candidate)):
        answer += 1

print(answer)
