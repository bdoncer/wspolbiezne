from multiprocessing import Process, Array

def mergeSort(arr, start_id, end_id):
    if end_id != start_id:

        # Finding the mid of the array
        mid = (end_id - start_id) // 2


        # Sorting the first half
        mergeSort(arr,start_id, mid)

        # Sorting the second half
        mergeSort(arr, mid + 1, end_id)


        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = Array('i',[12, 11, 13, 5, 6, 7])
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", end="\n")
    printList(arr)
