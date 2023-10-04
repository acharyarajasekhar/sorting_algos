def insertion_sort(arr):
    size = len(arr)
    
    for i in range(1, size):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = current
        

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    print("Given array : " )
    print(elements)
    insertion_sort(elements)
    print("Sorted array : " )
    print(elements)
