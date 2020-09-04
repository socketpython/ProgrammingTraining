def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            print(j, end=' ')
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print()


def main():
    arr = [64, 34, 45, 13, 54, 76, 8, 23, 34, 6567, 7, 8, 9, 3, 2]
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
