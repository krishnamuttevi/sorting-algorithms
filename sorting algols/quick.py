def quicksort(arr, start, end):
    if start < end:
        piv = pivot(arr, start, end)
        quicksort(arr, start, piv - 1)
        quicksort(arr, piv + 1, end)

def pivot(arr, start, end):
    piv = arr[start]
    i = start + 1 
    j = end
    while True:
        # Move `i` to the right as long as elements are smaller than or equal to the pivot
        while i <= end and arr[i] <= piv:
            i += 1
        # Move `j` to the left as long as elements are greater than the pivot
        while j >= start and arr[j] > piv:
            j -= 1
        # If `i` and `j` cross, break out of the loop
        if i >= j:
            break
        # Swap elements at `i` and `j`
        arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot element with the element at `j` to place the pivot in its correct position
    arr[start], arr[j] = arr[j], arr[start]
    
    return j

arr = list(map(int, input().split()))
quicksort(arr, 0, len(arr) - 1)
print(arr)
