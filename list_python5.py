#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

n=int(input("How many string input do you wanna to store: "))
p=[]
c=0
print("Strings are: ")
for i in range(n):
    p.append(input())
for i in range(n):
    if((len(p[i])>=2) and p[i][0]==p[i][-1]):
        c+=1
print("Sample List: ",p)
print("Expected Result: ",c)
