#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor 
#Sample String : 'abc'
#Expected Result : 'abcing' 
#Sample String : 'string'
#Expected Result : 'stringly'

s=input("Enter the string: ")
p=len(s)
c=''
if(p<3):
    print(s)
else:
    if(s[p-3:]=='ing'):
        k=[s,'ly']
        k=c.join(k)
        print(k)
    else:
        k=[s,'ing']
        k=c.join(k)
        print(k)
        







        