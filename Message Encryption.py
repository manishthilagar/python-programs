s = input()
col = int(input()) 
count = 0 
arr = []  
for i in range(col): 
  if i%2 == 0 : 
    a = [] 
    for j in range(col): 
      a.append(s[count]) 
      count = count+1 
    arr.append(a) 
  else: 
    a = [] 
    for j in reversed(range(0,3)): 
      a.append(s[count]) 
      count = count+1 
    arr.append(a[::-1]) 
l = [] 
for i in range(col): 
  for j in range(col): 
    l.append(arr[j][i]) print(l)
