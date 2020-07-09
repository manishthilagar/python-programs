from functools import reduce
from operator import mul
a=[int(i) for i in input().strip()]
l=reduce(mul,a)
for j in l:
  print(round(j),end=" ")
