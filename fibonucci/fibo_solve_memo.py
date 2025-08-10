def fib_memo(n, memo={}):
    print(f"ค่าปัจจุบัน fib_memo({n})")
    
    if n in memo: # ← (1) ตรวจว่าคำนวณแล้วหรือยัง
        print(f"  พบใน memo: fib({n}) = {memo[n]}")
        return memo[n]  #     ถ้ามีก็ return ได้เลย 
    

    if n <= 1: # ← (2) ตรวจว่าเป็น base case ไหม (F(0) หรือ F(1))
        print(f"  กรณีฐาน: fib({n}) = {n}")
        return n #     ถ้าใช่ return เลย
    # (3) ถ้าไม่ใช่ทั้งสองกรณี → ต้องคำนวณก่อน!
    print(f"  คำนวณ fib({n-1}) + fib({n-2})")
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    
    print(f"  เก็บค่า fib({n}) = {memo[n]} ลง memo")
    return memo[n]  # ← (4) return หลังจากคำนวณเสร็จ

if __name__ == "__main__":
    print(f"\nผลลัพธ์สุดท้าย: {fib_memo(10)}")
