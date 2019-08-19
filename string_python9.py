#Write a Python program to remove the nth index character from a nonempty string.

s=input("Enter the string: ")
k=[]
p=0
c=''
for i in s:
    p+=1
print("Your string is of 0 -", p-1 ,"index characters")
n=int(input("Which index character do you wanna to remove: "))
for i in s:
    k.append(i)
del k[n]
k=c.join(k)
print(k)