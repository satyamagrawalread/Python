#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
#Sample data : {'1':['a','b'], '2':['c','d']}
#Expected Output: 
#ac
#ad
#bc
#bd

p=[]
k=[]
n=int(input("How many letters do you wanna to give in list1: "))
for i in range(n):
    p.append(input("key "+str(i+1)+": "))
m=int(input("How many letters do you wanna to give in list2: "))
for i in range(m):
    k.append(input("key "+str(i+1)+": "))
d={'1':p, '2':k}
print(d)
for i in d['1']:
    for j in d['2']:
        print(i+j)
