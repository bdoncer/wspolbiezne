from multiprocessing import Pool, Value, Process


def add_element(element,sum):
    sum.value += element

def sum_elements(array):
    sum = Value('i', 0)
    processes = []
    for i in range(len(array)):
        processes.append(Process(add_element(array[i],sum)))

    for i in range(len(processes)):
        processes[i].start()

    for i in range(len(processes)):
        processes[i].join()

    return sum.value

if __name__ == '__main__':
    array = [3, 6, 4, 6, 3, 5, 3, 54, 52, 432, 45, 34]

    print(sum_elements(array))
