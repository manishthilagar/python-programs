''' In a college ,  a professor is strict and mandates that at least M students out of the total N students must arrive on time to his class.Else he would cancel the class. The start time of the class is also passed as the input.The individual arrival time for N students is also passed as input in 24 hours format.

The program must print if the class was cancelled or not.

Example 1:

Input:
5 3
9:30
9:30 9:38 9:31 9:32 9:31
Output:
Yes
Explanation:
4 out of the students arrived late, which means only one arrived on time. As the professor has mandated 3 out of the 5 must arrive on time, the class was cancelled and hence Yes is printed as the output.
'''


n = input().split()
check = input().split(":") 
time  = input().split()
count = 0
c = 0
#print(n,check,time)
for i in range(int(n[0])):
    c = 0
    c = time[i].split(":")
    #print(c[0],check[0],c[1], check[1])
    if int(c[0]) > int(check[0]):
        count += 1
        #print(count)
    else:
        if int(c[0]) == int(check[0]) and int(c[1]) > int(check[1]):
            count += 1
            #print(count)
   
n[0] = int(n[1]) - count         
if n[0] >= int(n[1]):
    print("No")
else:
    print("Yes")
        
   
