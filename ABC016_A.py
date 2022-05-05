import io
import sys

_INPUT = """\
6
1 1
2 29
12 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  M,D=map(int,input().split())
  if (M%D==0): print('YES')
  else: print('NO')