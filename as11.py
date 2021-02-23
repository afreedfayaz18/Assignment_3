nl=[]
z=-1
y=int(input("Enter the limit :"))
for x in range(z,y):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))