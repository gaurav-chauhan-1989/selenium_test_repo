import os.path

filename="io.txt"                                              # Filename
fi=os.path.join("D:/Backup", filename)                         # Give path to the file

f=open(fi, "w+")
f.write("This is shekhar chauhan \nThis is gaurav chauhan")
f.close()

f=open("io.txt","r+")
str=f.read()
print(str)
f.close()
f=open("io.txt","a")
f.write("\n This is archana chauhan")
f.close()
f=open("io.txt","r+")
for i in f:
    print(i)





