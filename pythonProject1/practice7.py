from collections import Counter
N, X = map(int, input().split())
A = list(map(int, input().split()))
strX = ''

for i in range(N):
    if A[i] < X:
        strX += str(A[i]) + ''


print(N)
print(A)
print(X)
print(strX)

