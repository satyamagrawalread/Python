#Write a Python program to map two lists into a dictionary.

n=int(input("How many keys do you wanna to give: "))
k=[]
v=[]
print("Write "+str(n)+" keys: ")
for i in range(1,n+1):
    k.append(input("Key "+str(i)+": "))
print("Write its values: ")
for i in range(1,n+1):
    v.append(input("Value"+str(i)+": "))
d={}
for i in range(n):
    d[k[i]]=v[i]
print(k)
print(v)
print(d)


