from multiprocessing import Pool

def multiply_2(el1,el2):
    return el1*el2


def pow(x, n):
    array = [x for i in range(n)]

    while len(array) > 1:
        pool = Pool(len(array)//2 + 1)
        elements = []
        i = 0
        while i < len(array):
            if i + 1 == len(array):
                elements.append([array[i], array[i]])
            else:
                elements.append([array[i], array[i + 1]])
            i += 2
        array = pool.starmap(multiply_2,elements)
        pool.close()
        pool.join()
    return array


if __name__ == '__main__':
    print(pow(4,2))