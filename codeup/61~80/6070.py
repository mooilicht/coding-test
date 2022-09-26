"""
[기초-조건/선택실행구조] 월 입력받아 계절 출력하기
https://codeup.kr/problem.php?id=6070

월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall

입력 예시
12

출력 예시
winter
"""
a = int(input())

if 3 <= a <= 5:
    print("spring")
elif 6 <= a <= 8:
    print("summer")
elif 9 <= a <= 11:
    print("fall")
else:
    print("winter")
