l1=[]
numbers=0
numbers=int(input("enter the elements :"))
for i in range(numbers):
	l1.append(int(input("enter the values :")))
print(l1) 
def find_len(l1):
    length = len(l1) 
    l1.sort() 
    print("Second Smallest element is:", l1[1]) 
Largest = find_len(l1) 