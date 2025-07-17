import matplotlib.pyplot as plt
import time
import quick
import redix
import Select_

# ขนาดของอาร์เรย์
x = [10, 20, 30, 40, 50]

# เก็บเวลาสำหรับทั้ง 3 เคส
result_best = {'Select': [], 'Radix': [], 'Quick': []}
result_worst = {'Select': [], 'Radix': [], 'Quick': []}
result_avg = {'Select': [], 'Radix': [], 'Quick': []}

# สุ่มเพียงครั้งเดียว สร้าง data สำหรับทุกขนาดล่วงหน้า
generated_data = {}
base_array = [i for i in range(1, 101)]  # ใช้เลขคงที่ ไม่ใช้ random
for size in x:
    sub_array = base_array[:size]
    generated_data[size] = {
        'best': sorted(sub_array),
        'worst': sorted(sub_array, reverse=True),
        'avg': sub_array[:]  # average ก็คือลำดับเดิมที่ยังไม่เรียง
    }

# เริ่มการวัดเวลา
for size in x:
    # ---- Best Case ----
    arr = generated_data[size]['best'][:]
    start = time.perf_counter()
    Select_.SelectSort.selection_sort_desc(arr[:])
    result_best['Select'].append((time.perf_counter() - start) * 1000)

    start = time.perf_counter()
    redix.RadixSort.radix_sort(arr[:])
    result_best['Radix'].append((time.perf_counter() - start) * 1000)

    start = time.perf_counter()
    quick.QuickSort.quick_sort(arr[:], 0, len(arr) - 1)
    result_best['Quick'].append((time.perf_counter() - start) * 1000)

    # ---- Worst Case ----
    arr = generated_data[size]['worst'][:]
    start = time.perf_counter()
    Select_.SelectSort.selection_sort_desc(arr[:])
    result_worst['Select'].append((time.perf_counter() - start) * 1000)

    start = time.perf_counter()
    redix.RadixSort.radix_sort(arr[:])
    result_worst['Radix'].append((time.perf_counter() - start) * 1000)

    start = time.perf_counter()
    quick.QuickSort.quick_sort(arr[:], 0, len(arr) - 1)
    result_worst['Quick'].append((time.perf_counter() - start) * 1000)

    # ---- Average Case ----
    arr = generated_data[size]['avg'][:]
    start = time.perf_counter()
    Select_.SelectSort.selection_sort_desc(arr[:])
    result_avg['Select'].append((time.perf_counter() - start) * 1000)

    start = time.perf_counter()
    redix.RadixSort.radix_sort(arr[:])
    result_avg['Radix'].append((time.perf_counter() - start) * 1000)

    start = time.perf_counter()
    quick.QuickSort.quick_sort(arr[:], 0, len(arr) - 1)
    result_avg['Quick'].append((time.perf_counter() - start) * 1000)

# -----------------------
# แสดงผลในกราฟ
# -----------------------
plt.figure(figsize=(12, 8))

# Best Case
plt.plot(x, result_best['Select'], label='Select (Best)', linestyle='--', marker='o', color='blue')
plt.plot(x, result_best['Radix'], label='Radix (Best)', linestyle='--', marker='o', color='green')
plt.plot(x, result_best['Quick'], label='Quick (Best)', linestyle='--', marker='o', color='red')

# Worst Case
plt.plot(x, result_worst['Select'], label='Select (Worst)', linestyle=':', marker='s', color='blue')
plt.plot(x, result_worst['Radix'], label='Radix (Worst)', linestyle=':', marker='s', color='green')
plt.plot(x, result_worst['Quick'], label='Quick (Worst)', linestyle=':', marker='s', color='red')

# Average Case
plt.plot(x, result_avg['Select'], label='Select (Avg)', marker='^', color='blue')
plt.plot(x, result_avg['Radix'], label='Radix (Avg)', marker='^', color='green')
plt.plot(x, result_avg['Quick'], label='Quick (Avg)', marker='^', color='red')

plt.title('Empirical Comparison: Best, Worst, Average Cases')
plt.xlabel('Array Size (n)')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
