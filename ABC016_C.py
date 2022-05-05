import io
import sys

_INPUT = """\
6
3 2
1 2
2 3
3 3
1 2
1 3
2 3
8 12
1 6
1 7
1 8
2 5
2 6
3 5
3 6
4 5
4 8
5 6
5 7
7 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    A,B=map(int,input().split())
    A-=1; B-=1
    G[A].append(B)
    G[B].append(A)
  for i in range(N):
    print(bfs(G,i).count(2))