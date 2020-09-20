def insertionSort(arr):
    for i in range(1,len(arr),1):
        j=i-1
        temp=arr[i]
        while j>=0 and temp <arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr

if __name__ == "__main__":
    arr=[20 , 18 , 12 , 8 , 5 , -2]
    print(insertionSort(arr))
    list

