n, k = map(int, input().split())
top = 1
bottom = 1

for i in range(2, n + 1):
    top *= i
for i in range(2, k + 1):
    bottom *= i
for i in range(2, n - k + 1):
    bottom *= i

print(round(top / bottom))

# or

import math

n, k = map(int, input().split())
print(round(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))
