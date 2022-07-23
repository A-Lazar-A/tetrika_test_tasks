def task1(array):
    if isinstance(array, list):
        for i in range(len(array)):
            if array[i] == 0:
                return i
    elif isinstance(array, str):
        index = array.find('0')
        if index == -1:
            return 'There isn\'t 0'
        else:
            return index
    return 'There isn\'t 0'


def main():
    print(task1("111111111110000000000000000"))
    print(task1([1, 1, 1, 1, 1, 0, 0]))
    print(task1("111111"))
    print(task1([1, 1, 1, 1, 2, 2, 2, 2]))


if __name__ == '__main__':
    main()
