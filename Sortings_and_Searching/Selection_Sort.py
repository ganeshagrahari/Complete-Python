def selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
                arr[i],arr[mini]= arr[mini],arr[i]

arr = [10,40,2,17]
selection(arr)                
print("the sorted array is :",arr)