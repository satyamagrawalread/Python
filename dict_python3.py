#Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

#Sample Dictionary : 
#dic1={1:10, 2:20} 
#dic2={3:30, 4:40} 
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("There are three dictionary in which you have to fill keys and values")
dic1={}
dic2={}
dic3={}
d={}
n=int(input("How many keys do you wanna to give in dictionary1: "))
for j in range(1,n+1):
    p=input("Key"+str(j)+": ")
    dic1[p]=input("Its Value: ")
n=int(input("How many keys do you wanna to give in dictionary2: "))
for j in range(1,n+1):
    p=input("Key"+str(j)+": ")
    dic2[p]=input("Its Value: ")
n=int(input("How many keys do you wanna to give in dictionary3: "))
for j in range(1,n+1):
    p=input("Key"+str(j)+": ")
    dic3[p]=input("Its Value: ")
for i in dic1:
    d[i]=dic1.get(i)
for i in dic2:
    d[i]=dic2.get(i)
for i in dic3:
    d[i]=dic3.get(i)
print("After concatenate of all dictionary: ",d)


    






