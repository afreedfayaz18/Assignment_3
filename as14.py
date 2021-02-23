def search(arr, n, x):
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
arr=[]
numbers=0
numbers=int(input("enter the elements :"))
for i in range(numbers):
	arr.append(int(input("enter the values :")))    
print(arr)
x =0
x=int(input("Enter the element want to searach :"))
n = len(arr)

result = search(arr, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)