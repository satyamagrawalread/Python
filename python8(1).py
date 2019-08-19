#Write a Python program to display the first and last colors from the list.(Take list of color input by the user.)

n=int(input("no. of colors in a list: "))
c=[]
for i in range(n):
    c.append(input())
print("First and Last colors are: ",c[0],"and",c[-1])