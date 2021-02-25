A=[]
numbers=0
numbers=int(input("enter the elements :"))
for i in range(numbers):
    A.append(int(input("enter the values :")))
print(A) 
import sys 
for i in range(len(A)): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j         
    A[i], A[min_idx] = A[min_idx], A[i] 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i])
