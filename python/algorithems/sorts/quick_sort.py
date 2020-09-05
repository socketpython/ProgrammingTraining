def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low >= high:
        return
    index = partition(arr, low, high)
    quick_sort(arr, low, index - 1)
    quick_sort(arr, index + 1, high)


def main():
    arr = [64, 34, 45, 13, 54, 76, 8, 23, 34, 6567, 7, 8, 9, 3, 2]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    main()
