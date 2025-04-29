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
