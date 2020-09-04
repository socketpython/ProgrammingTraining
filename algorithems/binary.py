def binary_search(arr, e):
    low = 0
    high = len(arr) - 1
    while low <= high:
        print("Iteration!")
        middle = (low + high) // 2
        if arr[middle] == e:
            return middle
        elif arr[middle] > e:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 8))
    print(binary_search(arr, 15))


if __name__ == '__main__':
    main()
