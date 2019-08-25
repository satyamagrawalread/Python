#Write a Python script to check if a given key already exists in a dictionary.

d={}
n=int(input("How many keys do you wanna to add in a dictionary: "))
for i in range(n):
    k=input("Key: ")
    d[k]=input("Value: ")
print(d)
p=input("Write a key which you wanna to find: ")
for i in d:
    if(i==p):
        print("key exists")
        p=1
if(p!=1):
    print("Key does not exist")

