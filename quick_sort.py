from multiprocessing import Process, Array

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        p1 = Process(quick_sort(array, low, pi - 1))
        p2 = Process(quick_sort(array, pi + 1, high))

        p1.start()
        p2.start()
        p1.join()
        p2.join()


array = Array('i',[10, 7, 8, 9, 1, 11, 5])

if __name__ == '__main__':
    quick_sort(array, 0, len(array) - 1)

    print(f'Sorted array: {array[:]}')