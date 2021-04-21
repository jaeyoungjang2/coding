count = int(input())
lst = list(input().split())

numberLst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
dic = {i: True for i in numberLst}

res_lst = []


def check(res, strand):
    if strand == ">" and int(res[-2]) > int(res[-1]):
        return True
    elif strand == "<" and int(res[-2]) < int(res[-1]):
        return True
    else:
        return False


def go(res, index):
    # res의 개수가 count + 1와 같을 경우 return
    if len(res) == count + 1:
        res_lst.append(res)
        return
    # res의 개수가 count + 1와 다를 경우

    for i in dic:
        if dic[i] == True:
            # 새로운 값을 추가한 후, 부등호가 들어간 식이 일치하는지 확인
            if check(res + i, lst[index]):
                dic[i] = False
                # 일치한다면 재귀함수로 넘겨준다.
                go(res + i, index + 1)
                dic[i] = True


for i in numberLst:
    res = i
    dic[i] = False
    go(res, 0)
    dic[i] = True
print(max(res_lst))
print(min(res_lst))