def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = []

print("Enter numbers. Type 'done' to finish.")

while True:
    input_data = input("Enter a number (or 'done' to finish): ")

    if input_data.lower() == 'done':
        break

    try:
        number = int(input_data)
        arr.append(number)
        heapSort(arr)
        print("Sorted data:", arr)
    except ValueError:
        print("Please enter a valid number.")

print("Final sorted data:", arr)


