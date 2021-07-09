''' An integer number is the input, find the sum of power of its next position of the each number.

Assumption

The input should always be greater than 9. Do not use built-in functions.

Example

Input: 1234

Output. 94

Explanation

1234> (1^2)+(2^3)+(3^4) + (4^1) => 1 +8+81+ 4 =

18 '''



n = input()
c=0
for i in range(len(n)):

    if i<len(n)-1:
        c += int(n[i])**int(n[i+1])
    else:
        c += int(n[i])**int(n[0])
print(c)
