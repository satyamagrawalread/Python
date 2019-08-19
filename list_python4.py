#Write a Python program to get the smallest number from a list.

n=int(input("How many nos. do you wanna to store in a list: "))
p=[]
print("nos. are: ")
for i in range(n):
    p.append(int(input()))
for i in range(1,n):
    if(p[i]<p[0]):
        t=p[i]
        p[i]=[0]
        p[0]=t
print("Smallest no.: ",p[0])