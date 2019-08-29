#Write a Python program to combine two dictionary adding values for common keys. Go to the editor
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1={}
d2={}
d={}
t={}
n=int(input("How many keys do you wanna to provide in dictionary1:"))
for i in range(n):
    p=input("Key"+str(i+1)+": ")
    d1[p]=int(input("Its value: "))
n=int(input("How many keys do you wanna to provide in dictionary2:"))
for i in range(n):
    p=input("Key"+str(i+1)+": ")
    d2[p]=int(input("Its value: "))
for i in d1:
    for j in d2:
        if(i==j):
            t[i]=d1[i]+d2[i]
for i in d1:
    d[i]=d1[i]
for i in d2:
    d[i]=d2[i]
for i in t:
    d[i]=t[i]
print(d1)
print(d2)
print(d)

