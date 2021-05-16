list1 = [12, -7, 5, 64, -14] 
list2 = [12, 14, -95, 3] 
list=[]
for n in list1:
    if n>0:
        print(n,end=",")       
print("\n")
for m in list2:
    if m>0:
        list.append(m)
print(list)
