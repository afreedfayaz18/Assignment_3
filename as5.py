def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])

list1=input("Enter the elements :")
data =[]
bubbleSort(data)
print('Sorted Array in Asc ending Order:')
print(list1)