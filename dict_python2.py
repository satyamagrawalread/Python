#Write a Python script to add a key to a dictionary. Go to the editor
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

d={}
n=int(input("How many keys do you wanna to add in a dictionary: "))
for i in range(n):
    k=input("Key: ")
    d[k]=input("Value: ")
print(d)
print("Add a key and its value: ")
k=input("Key: ")
d[k]=input("Value: ")
print(d)