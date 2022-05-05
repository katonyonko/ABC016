import io
import sys

_INPUT = """\
6
1 0 1
1 1 2
1 1 0
1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C=map(int,input().split())
  if A+B==C and A-B==C: print('?')
  elif A+B==C: print('+')
  elif A-B==C: print('-')
  else: print('!')