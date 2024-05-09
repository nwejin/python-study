# import sys
# sys.stdin = open("input.txt", "r")

# 함수 작성 dfs (재귀)
def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1 # 실제 방문 표시
    # 표시를 안하면 무한 루프 발생

    for n in adj[c]:
        if not v[n]: #방문하지 않은 노드인 경우
            dfs(n)

# 함수 작성 bfs (queue)
def bfs(s):
    q = [] # 필요한 q, v[], 변수 생성

    q.append(s)   #Q에 초기 데이터(들) 삽입
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]: # 방문하지 않은 노드라면 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1 # 방문 표시


# 노드, 간선, 시작 번호 입력 받기
N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

# [1] 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)

print(v)
print(*ans_dfs)
print(*ans_bfs)