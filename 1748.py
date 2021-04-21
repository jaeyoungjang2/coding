input_count = int(input())

init = 1
strLength = 1
res = 0
while True:
    init *= 10
    temp = init-(init*0.1)
    if input_count < init-1:     
        
        init = init/10
        temp = input_count - init + 1
        res += temp*strLength
        
        break
    
    res += temp*strLength
    strLength += 1
print(int(res))
