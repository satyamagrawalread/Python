#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor 
#Sample String : 'restart'
#Expected Result : 'resta$t'

s=input("Enter the string: ")
p=len(s)
k=[]
c=''
for i in range(p):
        k.append(s[i])
for i in range(1,p):
        if(k[i]==k[0]):
                k[i]='$'
k=c.join(k)                                                     
print(k)