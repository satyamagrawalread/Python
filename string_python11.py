#Write a Python program to remove the characters which have odd index values of a given string.

s=input("Enter the string: ")
k=list(s)
p=len(s)
for i in range(1,int(p/2+1)):
    del k[i]
k=''.join(k)
print(k)
