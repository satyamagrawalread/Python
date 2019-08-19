#Write a Python program to sum all the items in a list.

n=int(input("How many nos. do you wanna to store in a list: "))
p=[]
sum=0
print("nos. are: ")
for i in range(n):
    p.append(int(input()))
for i in range(n):
    sum+=p[i]
print("Sum of nos. in the list: ",sum)