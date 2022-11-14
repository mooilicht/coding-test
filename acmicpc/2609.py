a, b = map(int, input().split())
prev_a = a
prev_b = b
while True:
    if a % b == 0:
        break
    remainder = a % b
    a = b
    b = remainder
gcd = b
print(gcd)
print(prev_a * prev_b // gcd)

# or

import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
