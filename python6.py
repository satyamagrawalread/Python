#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#Sample data : 3, 5, 7, 23
#Output : 
#List : ['3', ' 5', ' 7', ' 23'] 
#Tuple : ('3', ' 5', ' 7', ' 23')

p=[]
n=int(input("How many nos. do you wanna to give: "))
for i in range(n):
    p.append(input())
print(p)
print(tuple(p))