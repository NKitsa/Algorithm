import random as rn
import matplotlib.pyplot as plt
import time 
import quick
import redix
import Select_

x = [10, 20, 30, 40, 50]
y1 = []
y2 = []
y3 = []

for size in x:
    arry = [rn.randint(1, 100) for _ in range(size)]
    y1.append(Select_.SelectSort.selection_sort_desc(arry)*1000)
    y2.append(redix.RadixSort.radix_sort(arry)*1000);
    start = time.perf_counter()
    quick.QuickSort.quick_sort(arry,0,len(arry)-1);
    end = time.perf_counter()
    y3.append((end - start)*1000)

print(y1)
plt.plot(x, y1, label='Select Sort', marker='o', color='blue')
plt.plot(x, y2, label='Radix Sort', marker='o', color='green')
plt.plot(x, y3, label='Quick Sort', marker='o', color='red')

plt.title('Graph')
plt.xlabel('X (Lenght of Array) ')
plt.ylabel('Y (Time) ms ')
center_x = sum(x) / len(x) 
top_y = max(y1 + y2 + y3)   
balance = 0.006
font = 9
plt.text(x[len(x)-1]-2, y1[len(y1)-1] - balance, 'Select', color='blue', fontsize=font)
plt.text(x[len(x)-1]-2,     y2[len(y2)-1] - balance, 'Radix',  color='green', fontsize=font)
plt.text(x[len(x)-1]-2, y3[len(y3)-1] - balance, 'Quick',  color='red', fontsize=font)

plt.show()