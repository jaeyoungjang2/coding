import sys
cnt = list(map(int,sys.stdin.readline().rstrip().split()))
#a = 25
#b = 13
#c = 12

a = cnt[0]
b = cnt[1]
c = cnt[0] - cnt[1]

def confirm(cnt, number, index, res):
	while True:
		if cnt**index > number:
			break
		res += number // cnt**index
		index += 1
	return res

res_2 = confirm(2, a, 1, 0)
res_5 = confirm(5, a, 1, 0)
res_2b = confirm(2, b, 1, 0)
res_5b = confirm(5, b, 1, 0)
res_2c = confirm(2, c, 1, 0)
res_5c = confirm(5, c, 1, 0)

print(min(res_2-res_2b-res_2c,res_5-res_5b-res_5c))

print(min(res_2-res_2b-res_5c,res_5-res_5b-res_5c))