num = int(input())
numbers = list(map(int, input().split()))
count = 0
for n in numbers:
    check = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                check = False
        if check:
            count += 1
print(count)

# or

num = int(input())
numbers = list(map(int, input().split()))
count = 0

max_num = max(numbers)
sieve = [True] * max_num
sieve[0] = False
m = int(max_num**0.5)

for i in range(2, m + 1):
    if sieve[i - 1] == True:
        for j in range(i + i, max_num + 1, i):
            sieve[j - 1] = False

results = [i + 1 for i in range(len(sieve)) if sieve[i] == True]
for i in results:
    if i in numbers:
        count += 1

print(count)
