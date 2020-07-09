s=input()
l=len(s)
g=0
for i in range(l):
  g=l-i-1
  for j in range(l):
    if j==g:
      print(s[j],end="")
    elif j==i:
      print(s[j],end="")
    else:
      print(" ",end="")
  print(end="/n")    
  
