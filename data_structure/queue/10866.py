import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

for i in range(int(input())):
    command = input().split()
    keyword = command[0]
    if keyword == "push_front":
        queue.appendleft(command[1])
    elif keyword == "push_back":
        queue.append(command[1])
    elif keyword == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif keyword == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif keyword == "size":
        print(len(queue))
    elif keyword == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif keyword == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif keyword == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
