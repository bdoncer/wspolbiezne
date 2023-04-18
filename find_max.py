from multiprocessing import Process, Pool

def find_max(array):
    while (len(array) > 1):
        pool = Pool(len(array)//2+1)
        elements = []
        i = 0
        while i < len(array):
            if i + 1 == len(array):
                elements.append([array[i],array[i]])
            else:
                elements.append([array[i],array[i+1]])
            i+=2
        array = pool.starmap(find_max_from_2, elements)
        print(array)


def find_max_from_2(el1,el2):
    if el1 > el2:
        return el1
    return el2



T = [4,5,2,6,1,2,4,5,3,11,2,4,2,44,4,435,5,46,46,54]
if __name__ == '__main__':
    find_max(T)
