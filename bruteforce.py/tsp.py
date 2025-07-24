def subset_sum_brute_force(S, target):  # สร้างฟังก์ชันสำหรับหาชุดตัวเลขใน S ที่รวมกันได้เท่ากับ target โดยใช้วิธี brute-force ในการลองทุกทาง
    n = len(S)  # หาจำนวนสมาชิกในลิสต์ S
    total_subsets = 2 ** n # คำนวณจำนวน subset ทั้งหมด = 2^n 
    for mask in range(total_subsets):  # วนลูปทุกค่า mask ตั้งแต่ 0 ถึง 2^n - 1 เพื่อแทน subset แต่ละแบบ
        subset = []  # สร้างลิสต์ว่างไว้เก็บสมาชิกของ subset ปัจจุบัน
        total = 0  # ตัวแปรเก็บผลรวมของ subset ปัจจุบัน
        for i in range(n):  # วนลูปสมาชิกแต่ละตัวใน n
            if mask & (2 ** i):  # ตรวจว่าตำแหน่งบิตที่ i ของ mask เป็นยกกำลังไหม
                subset.append(S[i])  # ถ้าเลือก ก็เพิ่มตัวนั้นลงใน subset
                total += S[i]  # และเพิ่มค่าตัวนั้นเข้า total 
        if total == target:  # ถ้าผลรวมของ subset เท่ากับค่าที่ต้องการ
            print("พบ subset ที่รวมได้เท่ากับ", target, ":", subset)  # แสดง subset ที่เจอ
            return True  # คืนค่า True บอกว่าเจอแล้ว
    print("ไม่พบ subset ที่รวมได้เท่ากับ", target)  # ถ้าลองทุกกรณีแล้วยังไม่เจอ จะprint text ออกมาว่าไม่เจอโดยใส่ค่าคือเลข target
    return False  # คืนค่า False บอกว่าไม่พบ subset ที่รวมกันได้ target

# ทดสอบโปรแกรม
S = [3, 1, 7, 9, 5]  # กำหนดลิสต์ตัวเลขที่ต้องการหาชุดย่อย
target = 12  # กำหนดค่าผลรวมที่ต้องการหา
subset_sum_brute_force(S, target)  # เรียกใช้ฟังก์ชันเพื่อหาว่ามี subset ไหนรวมกันได้ target ไหม



