w, h, b = map(int, input().split())
print(f"{format(w*h*b/8/1024/1024, '.2f')} MB")
