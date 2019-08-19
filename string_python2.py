#Write a Python program to count the number of characters (character frequency) in a string. Go to the editor 
#Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s=input("Enter the string: ")
t={}
for i in s:
    t[i]=0
for i in s:
    t[i]+=1
print(t)
    
