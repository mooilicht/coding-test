for i in range(int(input())):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    min_num = min(a, b)
    max_num = max(a, b)
    if min_num == b:
        a_list, b_list = b_list, a_list
    result = 0
    for j in range(max_num - min_num + 1):
        sum = 0
        for k in range(j, min_num + j):
            sum += b_list[k] * a_list[k - j]
        result = max(result, sum)
    print(f"#{i+1} {result}")
