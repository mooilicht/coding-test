for i in range(int(input())):
    b = input()
    b_list = list(b)
    stack = []
    for j in b:
        if j == '(':
            stack.append(j)
            b_list.remove(j)
        elif j == ')' and '(' in stack:
            stack.pop()
            b_list.remove(j)
    if len(b_list) > 0 or len(stack) > 0:
        print('NO')
    else:
        print('YES')