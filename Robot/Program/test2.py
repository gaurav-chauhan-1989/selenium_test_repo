l = [1,5,0,5,7,0,3,0,10,11,12]
filtered = []
duplicate = []
l.sort()
for i in l:
    if i in filtered:
        duplicate.append(i)
    else:
        filtered.append(i)
print(filtered + duplicate)







