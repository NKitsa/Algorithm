class QuickSort:
    @staticmethod
    def swap_array(data, swap1, swap2):
        data[swap1], data[swap2] = data[swap2], data[swap1]

    @staticmethod
    def quick_sort(data, start, end):
        f = start
        r = end
        if end > start:
            pivot = data[end]
            while r > f:
                while f < end and data[f] < pivot and r > f:
                    f += 1
                while r > start and data[r] >= pivot and r >= f:
                    r -= 1
                if r > f:
                    QuickSort.swap_array(data, f, r)

            QuickSort.swap_array(data, f, end)
            QuickSort.quick_sort(data, start, f - 1)
            QuickSort.quick_sort(data, f + 1, end)
