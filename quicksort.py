def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]#基点的值
        
        less = [i for i in array[1:] if i <= pivot]
        #小于等于基点的集合

        greater = [i for i in array[1:] if i > pivot]
        #大于基点的集合

        return quicksort(less)+[pivot]+quicksort(greater)




    

#升序排序
def quicksortCsharp(array,left,right):
    if left == right:
        return
    else:
        pivot = left #基点索引
        i = left
        j = right
        while(i==j):
            if(array[i] >= array[j]):
                array[i],array[j] = array[j],array[i]
            #while(array[i] < array[pivot]):
                #i++
            #while(array[j] >= array[pivot]):
                #j--
def K3(arr,left,right):
    if(left >= right):
        return
    
    p = arr[left]
    i = left
    j = right
    while(i<j):
        while(arr[j]>=p and i<j):
            j -= 1
        while(arr[i]<=i and i<j):
            i += 1
        
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[left] = arr[i]
    arr[i] = p
    K3(arr,left,i-1)
    K3(arr,i+1, right)              
        
    
arr = [3,2,1]
K3(arr,0,2)
print(arr)
