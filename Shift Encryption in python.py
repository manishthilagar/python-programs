''' Anmol wants to encrypt the message  which is to be sent to his business partner.Binamol,  so he shifts every alphabet by X positions in forward direction and he adds Y ro every number in the message.

Given string value M of the message  and the values of X and Y, the program must print the encrypted message E.

->All alphabets will be lowercase.
->Spaces and special characters in message M should be reproduced as such in the encrypted message E.


Example 1:

Input:
call me at 10p.m
2
1
Output:
ecnn og cv 21r.o

Program:

'''



import string
words = input()
x = int(input())
y = input()
alph = list(string.ascii_lowercase)
num = ["0","1","2","3","4","5","6","7","8","9"]
out = []
e = 0
k = ""
for i in range(len(words)):
    for j in range(len(alph)):
        if words[i] == alph[j]:
            e = 0
            e = j + x
            if e < 25:
                out.append(alph[e])
            else:
                e = e - 26
                out.append(alph[e])
    if words[i] == " " or words[i] == ".":
        out.append(words[i])
    else:
        for l in range(len(num)):
            #print(words[i],num[l])
            if words[i] == num[l]:
                #print(words[i])
                k = words[i]
                k = int(k)
                #words[i] = int(words[i])
                #print(k)
                e = k + int(y)
                out.append(str(e))
    
            
            
                

s = ""
for i in out:
    s += i
    #print(s)
print(s)


