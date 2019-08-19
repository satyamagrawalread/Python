#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor 
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

s=input("Write a sentence: ")
k=s.split()
a,b=0,0
for i in k:
        if(i=='not'):
                a=k.index('not')
        if(i=='poor'):
                b=k.index('poor')
if(b>a):
        k[a]='good'
        del k[a+1:b+1]
        c=' '
        k=c.join(k)
        print(k)
else:
        c=' '
        k=c.join(k)
        print(k)