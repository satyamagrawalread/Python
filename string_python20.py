#Write a Python function to reverses a string if it's length is a multiple of 4.

s=input("Enter a string: ")
p=len(s)
if(p%4==0):
    for i in range(0,p/2):
        s[i],s[p-i-1]=s[p-i-1],s[i]
print(s)
