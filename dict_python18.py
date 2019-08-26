# Write a Python program to check a dictionary is empty or not. 

n=int(input("How many keys do you wanna to give: "))
d={}
k=0
for i in range(1,n+1):
    p=input("Key "+str(i)+": ")
    d[p]=input("Its value: ")
for i in d:
    k+=1
if(k==0):
    print("Dictionary is empty.")
if(k!=0):
    print("Dictionary is not empty.")
    print(d)
