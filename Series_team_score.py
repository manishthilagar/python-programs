A=input().split()
B=input().split()
x=0
sum1=0
sum2=0
for i in range(len(a)):
  if A[x]<B[x]:
    sum1+=3
  if A[x]==B[x]:
    sum1+=1
    sum2+=1
  else:
  sum2+=3
x+=1  
  
print(sum1,sum2)  
  
