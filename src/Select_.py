import time
class SelectSort:
    def selection_sort_desc(arr):
        start = time.perf_counter()
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] > arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        end = time.perf_counter()
        return end - start;

