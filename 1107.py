import sys
# target = 100
target = int(input())
separate = int(input())
channel = -1
minus_channel = 0
plus_channel = 0
count = 1


lst = list(map(int,sys.stdin.readline().split()))
# lst = [0,1,2,3,4]

    

def confirm(channel):
    global lst
    
    for i in str(channel):
        if int(i) in lst:            
            return False
    return channel

if separate == 10:
    result = 1000000
else:
    # target에서 가장 근접한 수이면서, 리모컨의 키가 고장나지 않은 것을 검색
    while True:
        if confirm(minus_channel):
            channel = minus_channel
            break
        elif confirm(plus_channel):
            channel = plus_channel
            break
        minus_channel = target - count
        plus_channel = target + count
        
        
        count += 1

    result = len(str(channel))+ abs(target-channel)
    print(channel)


if result > target-100:
    print(target-100)
else:
    print(result)