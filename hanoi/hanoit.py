def tower_of_hanoi(n, source, destination, auxiliary):
    """
    แก้ไขปัญหา Tower of Hanoi โดยใช้การเรียกซ้ำ (Recursive)
    :param n: จำนวนจานที่ต้องการย้าย
    :param source: ชื่อเสาต้นทาง (เช่น 'A')
    :param destination: ชื่อเสาปลายทาง (เช่น 'C')
    :param auxiliary: ชื่อเสาสำรอง (เช่น 'B')
    """
    # กรณีฐาน (Base Case): ถ้ามีจานเดียว ให้ย้ายจากต้นทางไปปลายทางได้เลย
    if n == 1:
        print(f"ย้ายจานที่ 1 จาก {source} ไปยัง {destination}")
        return

    # ขั้นตอนที่ 1: ย้าย n-1 จานจาก Source ไป Auxiliary (ใช้ Destination ช่วย)
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    # ขั้นตอนที่ 2: ย้ายจานที่ n (ใบที่ใหญ่ที่สุด) จาก Source ไป Destination
    print(f"ย้ายจานที่ {n} จาก {source} ไปยัง {destination}")

    # ขั้นตอนที่ 3: ย้าย n-1 จานจาก Auxiliary ไป Destination (ใช้ Source ช่วย)
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# ----------------------------------------------------------------------
# ใช้โครงสร้าง if __name__ == "__main__": สำหรับรันโค้ดแสดงผล
# ----------------------------------------------------------------------

if __name__ == "__main__":
    # กำหนดจำนวนจานที่ต้องการทดสอบ
    number_of_disks = 4  # สามารถเปลี่ยนเป็น 3, 5, หรือจำนวนอื่น ๆ ได้

    print(f"--- การแก้ปัญหา Tower of Hanoi สำหรับจาน {number_of_disks} ใบ ---")
    
    # คำนวณจำนวนครั้งในการย้ายจานที่น้อยที่สุด
    min_moves = 2**number_of_disks - 1
    print(f"จำนวนครั้งในการย้ายจานน้อยที่สุด: {min_moves} ครั้ง\n")

    # เรียกใช้ฟังก์ชัน: ย้ายจาน n ใบ จากเสา A ไปเสา C โดยมีเสา B เป็นตัวช่วย
    tower_of_hanoi(number_of_disks, 'A', 'C', 'B')
    
    print("\n-----------------------------------------------------")
    print(f"การย้ายจาน {number_of_disks} ใบเสร็จสมบูรณ์")