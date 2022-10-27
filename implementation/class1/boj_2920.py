scale = [1, 2, 3, 4, 5, 6, 7, 8]
r_scale = list(reversed(scale))

play = list(map(int, input().split()))

if scale == play:
    print("ascending")
elif r_scale == play:
    print("descending")
else:
    print("mixed")
