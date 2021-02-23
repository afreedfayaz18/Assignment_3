def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
           
        if arr[mid] == x: 
            return mid  
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1 
    return -1 
arr=[]
numbers=0
numbers=int(input("enter the elements :"))
for i in range(numbers):
    arr.append(int(input("enter the values :")))
print(arr)     
x = 0
print(arr)
x =int(input("Enter the number :"))
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 