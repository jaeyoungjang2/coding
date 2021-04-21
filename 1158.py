from collections import deque
import sys
q = deque()
count_lst = sys.stdin.readline().rstrip().split()
for i in range(1,int(count_lst[0])+1):
	q.append(i)
print(count_lst)
target_index = int(count_lst[1])
index = 1
res_lst = []
while q:

	if index == target_index:
		res_lst.append(q.popleft())
		index = 1
	else:
		q.append(q.popleft())
		index += 1
print('<'+', '.join(map(str,res_lst))+'>')

