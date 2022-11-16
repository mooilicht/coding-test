from collections import deque

queue = deque()
n = int(input())

for i in range(1, n + 1):
    queue.append(i)

count = 0
while len(queue) > 1:
    count += 1
    if count % 2 == 0:
        queue.append(queue.popleft())
    else:
        queue.popleft()

print(queue[0])
