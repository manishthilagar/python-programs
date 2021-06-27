a,b=map(float, input().split())
if (a%5==0 and a+0.5<=b):
    b-=a+0.50
print ('%.2f'%b)     
