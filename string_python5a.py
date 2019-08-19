#Sample String : 'abc' 'xyz' 
#Expected Result : 'yxz bac'

p=[]
c=' '
for i in range(2):
    p.append(input("Enter the string: "))
t=p[0]
p[0]=p[1]
p[1]=t
k=[p[0][0],p[0][1],p[0][2:]]
t=k[0]
k[0]=k[1]
k[1]=t
l=''
p[0]=l.join(k)
k=[p[1][0],p[1][1],p[1][2:]] 
t=k[0]
k[0]=k[1]
k[1]=t
p[1]=l.join(k)
c=c.join(p)
print(c)