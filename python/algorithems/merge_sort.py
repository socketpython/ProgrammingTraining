def merge_sort(arr):
    print(arr)
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    merge_sort(L)
    merge_sort(R)

    left_index = right_index = merged_index = 0
    while left_index < len(L) and right_index < len(R):
        if L[left_index] < R[right_index]:
            arr[merged_index] = L[left_index]
            left_index += 1
        else:
            arr[merged_index] = R[right_index]
            right_index += 1
        merged_index += 1

    while left_index < len(L):
        arr[merged_index] = L[left_index]
        left_index += 1
        merged_index += 1
    while right_index < len(R):
        arr[merged_index] = R[right_index]
        right_index += 1
        merged_index += 1


def main():
    arr = [56, 678, 45, 234, 5346, 7645, 567, 465, 346, 34, 34, 7689]
    merge_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
