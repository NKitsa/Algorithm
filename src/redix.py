import time

class RadixSort:

    @staticmethod
    def get_max(arr):
        return max(arr)

    @staticmethod
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            digit = (arr[i] // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        for i in range(n):
            arr[i] = output[i]

    @staticmethod
    def radix_sort(arr):
        start = time.perf_counter()
        max_num = RadixSort.get_max(arr)
        exp = 1
        while max_num // exp > 0:
            RadixSort.counting_sort(arr, exp)
            exp *= 10
        end = time.perf_counter()
        return end - start
