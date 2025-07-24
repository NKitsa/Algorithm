def my_pop(lst):
    if len(lst) == 0:
        raise IndexError("pop from empty list")
    last_element = lst[-1]
    del lst[-1]
    return last_element
def subset_sum_backtrack(S, target):
    result = []
    
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])  # เจอชุดที่รวมเท่ากับ target ให้เก็บcopy ไว้
            return
        if total > target:
            return   
        for i in range(start, len(S)):
            path.append(S[i])
            backtrack(i + 1, path, total + S[i])  
            my_pop(path)  # ลบตัวที่เพิ่มเข้ามา เพื่อหาชุดอื่นต่อ

    backtrack(0, [], 0)

    if result:
        for subset in result:
            print("Found subset:", subset)
    else:
        print("No subset found with sum =", target)

if __name__ == "__main__":
    # ทดสอบ
    S = [3, 34, 4, 12, 5, 2]
    target = 20
    subset_sum_backtrack(S, target)
