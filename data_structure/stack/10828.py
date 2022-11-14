import sys
input=sys.stdin.readline

stack = []
for i in range(int(input())):
  command = input().split()
  keyword = command[0]
  if len(command) == 2:
    number = int(command[1])
  if keyword == 'push':
    stack.append(number)
  elif keyword == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
  elif keyword == 'size':
    print(len(stack))
  elif keyword == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif keyword == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      stack.pop()