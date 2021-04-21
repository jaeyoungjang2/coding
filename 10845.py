#push X: 정수 X를 큐에 넣는 연산이다.
#pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 큐에 들어있는 정수의 개수를 출력한다.
#empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
#front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


from collections import deque
import sys
q = deque()
count = int(sys.stdin.readline().rstrip())
for i in range(count):
	cmd_lst = sys.stdin.readline().rstrip().split()
	if cmd_lst[0] == 'push':
			q.append(cmd_lst[1])
	elif cmd_lst[0] == 'size':
		print(len(q))
	elif q:
		if cmd_lst[0] == 'pop':
			print(q.popleft())
		elif cmd_lst[0] == 'empty':
			print(0)
		elif cmd_lst[0] == 'front' and q:
			print(q[0])
		elif cmd_lst[0] == 'back' and q:
			print(q[-1])
		elif cmd_lst[0] == 'empty':
			print(0)
	elif cmd_lst[0] == 'empty':
			print(1)
	else:
		print(-1) 
