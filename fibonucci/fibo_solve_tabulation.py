def fib_tab(n):
    # ถ้า n เป็น 0 หรือ 1 ให้ return ค่าตรง ๆ เลย (base case)
    if n <= 1:
        return n

    # สร้าง list (dp table) ขนาด n+1 เพื่อเก็บค่าของ Fibonacci แต่ละลำดับ
    # เริ่มทำงานจากตัวแรกคือ 0
    dp = [0] * (n + 1)

    # กำหนดค่าเริ่มต้นของ Fibonacci: F(1) = 1
    dp[1] = 1

    # ใช้ loop เติมค่าของ Fibonacci ตั้งแต่ F(2) ถึง F(n)
    for i in range(2, n + 1):
        # ใช้สูตร: F(n) = F(n-1) + F(n-2)
        dp[i] = dp[i - 1] + dp[i - 2]

    # คืนค่าของ Fibonacci ลำดับที่ n
    return dp[n]

# เรียกใช้งานฟังก์ชัน เพื่อหาค่า Fibonacci ลำดับที่ 100 และแสดงผล
print(fib_tab(100))
