def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right);
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)
    

def partition(arr, left, right):
    i, j = left, right-1
    pivot = arr[right]
    
    while i < j and arr[i] < pivot:
        i += 1
        
    while j > i and arr[j] > pivot:
        j -= 1
        
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]
        
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i
    
    
if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    print("Given array : " )
    print(elements)
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array : " )
    print(elements)
