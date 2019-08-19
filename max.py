#Write a python program to take n numbers from user and the print the largest number.
n=int(input("How many numbers do you wanna to give: "))
print("Enter ",n," numbers: ")
k=[]
for i in range(n):
    k.append(int(input()))
max=k[0]
for i in k:
    if(i>max):
        max=i
print("Largest no.: ",max)