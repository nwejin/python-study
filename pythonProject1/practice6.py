from collections import Counter

# N = int(input())
# M = list(map(int, input().split()))
# V = int(input())
#
# print(M.count(V))

N = int(input())
M = list(map(int, input().split()))
V = int(input())


print(Counter(M)[V])