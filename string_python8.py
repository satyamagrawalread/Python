#Write a Python function that takes a list of words and returns the length of the longest one.
 
n=int(input("How many words do you wanna to give: "))
k=[]
d=[]
for i in range(n):
    k.append(input())
for i in k:
    p=i
    c=0
    for j in p:
        c+=1
    d.append(c)
print("Length of the longest word: ",max(d))


