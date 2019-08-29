#Write a Python program to print all unique values in a dictionary. Go to the editor
#Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

d={}
k=[]
t=[]
n=int(input("How many keys do you wanna to provide in a dictionary: "))
for i in range(n):
    p=input("Key"+str(i+1)+": ")
    d[p]=int(input("Its value: "))
    k.append(d[p])
for i in k:
        g=0
        for j in k:
                if(i==j):
                        g+=1
        if(g==1):
                t.append(i)
print(d)
print("Set of unique values: ",set(t))


