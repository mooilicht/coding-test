a, b, c = map(int, input().split())
result = a if a < b else b
print(result if result < c else c)
