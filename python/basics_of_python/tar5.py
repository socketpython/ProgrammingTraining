def tar(file_path=None):
    if file_path == None:
        print("the func should get a file_path")
        return
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    to_int = []
    for i in data:
        to_int.append(int(i))
    stage_three(to_int)


def stage_two(arr):
    res = []
    for i in range(len(arr)):
        res.append(arr.pop(arr.index(min(arr))))
    return res


def stage_three(arr):
    a = bubble_sort(arr)
    b = insertion_sort(arr)
    c = selection_sort(arr)
    print(f"Bubble: {a},\nInsertion: {b},\nSelection: {c}")
    return


def bubble_sort(a):
    arr = a[:]
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


def insertion_sort(a):
    arr = a[:]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def selection_sort(a):
    arr = a[:]
    counter = 0
    for i in range(len(arr)-1):
        current_arr = arr[counter:]
        current_min = min(current_arr)
        pos = arr.index(current_min)
        arr.insert(counter, arr.pop(pos))
        counter += 1
    return arr


tar(r"C:/Users/Elad Levi/Desktop/a.txt")
