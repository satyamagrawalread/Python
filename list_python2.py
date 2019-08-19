#Write a Python program to multiply all the items in a list.

n=int(input("How many nos. do you wanna to store in a list: "))
p=[]
m=1
print("nos. are: ")
for i in range(n):
    p.append(int(input()))
for i in range(n):
    m*=p[i]
print("After multiplication: ",m)