#Write a Python program to count the occurrences of each word in a given sentence.

k=input("Write a sentence: ").split()
p={}
for i in k:
    c=0
    for j in k:
        if(i==j):
            c+=1
    p[i]=c
print(p)