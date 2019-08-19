# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor 
#Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
#In this program, use only small letter alphabet (No special character)

s=input("Enter the string: ")
a=[]
d={}
for i in range(26):
    a.append(0)
for i in s:
    p=ord(i)-97
    a[p]+=1
for i in range(26):
    k=chr(i+97)
    if(a[i]>0):
        d[k]=a[i]
print(d)

