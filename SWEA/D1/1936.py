# 1대1 가위바위보
a, b = map(int, input().split())
if a == b + 1 or (a == 1 and b == 3):
    print("A")
elif b == a + 1 or (b == 1 and a == 3):
    print("B")
