import io
import sys

_INPUT = """\
6
-2 0 2 0
4
1 1
-1 1
-1 -1
1 -1
-3 1 3 1
8
2 2
1 2
1 0
-1 0
-1 2
-2 2
-2 -1
2 -1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  Ax,Ay,Bx,By=map(int,input().split())
  N=int(input())
  t=[list(map(int,input().split())) for _ in range(N)]
  c=0
  for i in range(N):
    Cx,Cy=t[i]
    Dx,Dy=t[(i+1)%N]
    if Ax==Bx:
      if Cx==Dx: continue
      else:
        if min(Cx,Dx)<=Ax<=max(Cx,Dx) and min(Ay,By)<=(Cy-Dy)/(Cx-Dx)*Ax+(Cx*Dy-Cy*Dx)/(Cx-Dx)<=max(Ay,By): c+=1
    else:
      if Cx==Dx:
        if min(Ax,Bx)<=Cx<=max(Ax,Bx) and min(Cy,Dy)<=(Ay-By)/(Ax-Bx)*Cx+(Ax*By-Ay*Bx)/(Ax-Bx)<=max(Cy,Dy): c+=1
      else:
        if (Cy-Dy)*(Ax-Bx)-(Ay-By)*(Cx-Dx)==0: continue
        x=-((Cx*Dy-Cy*Dx)*(Ax-Bx)-(Ax*By-Ay*Bx)*(Cx-Dx))/((Cy-Dy)*(Ax-Bx)-(Ay-By)*(Cx-Dx))
        if min(Ax,Bx)<=x<=max(Ax,Bx) and min(Cx,Dx)<=x<=max(Cx,Dx): c+=1
  print((c+2)//2)