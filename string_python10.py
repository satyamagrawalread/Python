#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

s=input("Enter a string: ")
k=list(s)
k[0],k[-1]=k[-1],k[0]
k=''.join(k)
print("New string is: ",k)