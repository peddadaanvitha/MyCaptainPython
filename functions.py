s=input("Please enter a string ")
def most_frequent(s):
    s1=set(s)
    d={}
    s2={}
    for i in s1:
        d[i]=s.count(i)
    s2=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
    for j in s2:
        print(j,"=","0",s2[j],end=" ")
most_frequent(s.lower())
