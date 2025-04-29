class Operations:
    def __init__(self) -> None:
        pass

    def sumNaturalsIterative(self, n) -> int:
        s = 0
        for i in range(1, n + 1):
            s += i
        return s

    def sumNaturalsGauss(self, n) -> int:
        s = n * (n + 1) // 2
        return s

    def sequentialSearch(self, arr, value) -> int:
        for i in range(len(arr)):
            if arr[i] == value:
                return i
        return -1

    def binarySearch(self, arr, value) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def bubbleSort(self, arr) -> None:
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def insertionSort(self, arr) -> None:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def selectionSort(self, arr) -> None:
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
