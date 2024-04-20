s = [1,2,3,0,7,0,5,0]
a = []
k = 0
for i in range(len(s)):
    if s[i]!=0:
        a.append(s[i])
        k +=1
for j in range(k, len(s)):
    a.append(0)

print(a)







