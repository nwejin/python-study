from collections import Counter

N = int(input())
N_list = list(map(int, input().split()))
v = int(input())

print(Counter(N_list)[v])