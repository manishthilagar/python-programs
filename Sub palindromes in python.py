s = input()
counter = 0
for i in range(len(s)):
  for j in range(i+1,len(s)+1):
    temp = s[i:j]
    if temp == temp[::-1]:
      counter+=1
print(counter)
