def lcs_dp_table(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            char1 = str1[i - 1]
            char2 = str2[j - 1]

            if char1 == char2:
                dp[i][j] = dp[i - 1][j - 1] + 1
                print(f" ตรงกัน: {char1} == {char2} → dp[{i}][{j}] = {dp[i][j]} (จาก dp[{i-1}][{j-1}] + 1)")
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                print(f" ไม่ตรงกัน: {char1} != {char2} → dp[{i}][{j}] = max(dp[{i-1}][{j}]={dp[i-1][j]}, dp[{i}][{j-1}]={dp[i][j-1]}) = {dp[i][j]}")

    return dp[len1][len2]

if __name__ == "__main__":
    a = "ABCBDAB"
    b = "BDCAB"

    ans = lcs_dp_table(a, b)
    print("\nความยาวของ LCS คือ:", ans)
