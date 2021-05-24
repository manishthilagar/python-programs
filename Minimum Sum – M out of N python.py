""" Given N positive integers, find the minimum sum S that can be obtained by adding exactly M out of the N integers. The program must print the value of the minimum sum S in Python.

Example 1:

Input:
5 2
9 2 1 5 4
Output:
3

Explanation :
Out of the five given numbers, the sum of 1+2=3 is the least sum and hence printed as the output """





N = input().split()
Dummy = 0
listt = []
s = 0
num = input().split()
print(num)
for i in range(len(num)):
    
    for j in range(len(num)):
        if int(num[i]) < int(num[j]):
            
            s = num[j]
            num[j] = num[i]
            num[i] = s
          
#N = int(N[1]) 

for i in range(int(N[1])):
    Dummy  = Dummy + int(num[i])
print(Dummy)
        
