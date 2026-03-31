# Viết script sinh test tại đây
import os
import random
import shutil

# Cấu hình bài toán
TEN_BAI = "HVUONG"
MOD = 20222023
TOTAL_TESTS = 10

def solve(i, j, k):
    # Tổng hàng từ i đến i+k-1: S_row = k*(2*i + k - 1) / 2
    # Tổng cột từ j đến j+k-1: S_col = k*(2*j + k - 1) / 2
    # Kết quả T = (S_row * S_col) % MOD
    
    def sum_range(start, length):
        # Tính [length * (2*start + length - 1)] / 2 % MOD
        term1 = length
        term2 = (2 * start + length - 1)
        
        # Vì chia 2, ta kiểm tra số nào chẵn để chia trước khi nhân
        if term1 % 2 == 0:
            res = (term1 // 2) % MOD
            res = (res * (term2 % MOD)) % MOD
        else:
            res = (term2 // 2) % MOD
            res = (res * (term1 % MOD)) % MOD
        return res

    s_row = sum_range(i, k)
    s_col = sum_range(j, k)
    return (s_row * s_col) % MOD

def create_test(test_idx, i_val, j_val, k_val):
    folder = f"{TEN_BAI}/test{test_idx:03d}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Ghi file INP
    inp_path = os.path.join(folder, f"{TEN_BAI}.INP")
    with open(inp_path, "w") as f:
        f.write(f"{i_val} {j_val} {k_val}")
    
    # Ghi file OUT
    out_path = os.path.join(folder, f"{TEN_BAI}.OUT")
    ans = solve(i_val, j_val, k_val)
    with open(out_path, "w") as f:
        f.write(str(ans))

def main():
    if os.path.exists(TEN_BAI):
        shutil.rmtree(TEN_BAI)
        
    # Test 1: Sample test
    create_test(1, 2, 1, 3)
    
    # Subtest 1: K nhỏ (K <= 1000) - 2 test còn lại
    create_test(2, 1, 1, 1) # Biên nhỏ nhất
    create_test(3, 1000, 1000, random.randint(500, 1000))
    
    # Subtest 2: K trung bình (K <= 10^6) - 4 test
    create_test(4, random.randint(1, 1000), random.randint(1, 1000), 10**6)
    for t in range(5, 8):
        create_test(t, random.randint(1, 1000), random.randint(1, 1000), random.randint(10**5, 10**6))
        
    # Subtest 3: K lớn (K <= 10^9) - 3 test
    create_test(8, 1, 1, 10**9) # Biên lớn nhất
    create_test(9, 999, 888, 123456789)
    create_test(10, random.randint(1, 1000), random.randint(1, 1000), random.randint(10**8, 10**9))

    print(f"Đã sinh thành công {TOTAL_TESTS} test cho bài {TEN_BAI}")

if __name__ == "__main__":
    main()