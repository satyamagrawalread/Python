#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor 
#Sample String : 'abc', 'xyz' 
#Expected Result : 'xyc abz'

p=[]
c=' '
for i in range(2):
    p.append(input("Enter the string: "))
k=[p[0][0:2],p[1][2:]]
l=''
k=l.join(k)
m=[p[1][0:2],p[0][2:]]
m=l.join(m)
p[0]=m
p[1]=k
c=c.join(p)
print(c)