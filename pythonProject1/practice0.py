T = int(input())


for i in range(T):
    a, b = input().split()
    a = int(a)
    b = str(b)
    for i in range(len(b)):
        print(a*b[i], end='') # ends는 공백 제거
    print()
