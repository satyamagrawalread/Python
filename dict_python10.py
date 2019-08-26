# Write a Python program to sum all the items in a dictionary.

p={}
n=int(input("How many items do you wanna to add/sum: "))
for i in range(1,n+1):
    p['data'+str(i)]=input("data"+str(i)+"value: ")
print(p)
c=p.values()
print(c)
s=0
for i in c:
    k=int(i)
    s+=k
print("Sum: ",s)

