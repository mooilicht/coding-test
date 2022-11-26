grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for index in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    total_list = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        total = a * 0.35 + b * 0.45 + c * 0.2
        total_list.append(total)
    score = total_list[k - 1]
    total_list.sort(reverse=True)
    result = grades[total_list.index(score) // (n // 10)]
    print(f"#{index} {result}")
