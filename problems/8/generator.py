# Viết script sinh test tại đây
import os
import random
import shutil

# Cấu hình bài toán
PROB_NAME = "DIVISIBLE"
TOTAL_TESTS = 10

def solve(n, k, arr):
    """
    Sử dụng Prefix Sum và Hash Map để đếm số dãy con có tổng chia hết cho k.
    Công thức: (prefix_sum[j] - prefix_sum[i]) % k == 0  => prefix_sum[j] % k == prefix_sum[i] % k
    """
    remainder_counts = {0: 1}  # Ban đầu có 1 tổng bằng 0 (trước khi bắt đầu dãy)
    current_prefix_sum = 0
    total_count = 0
    
    # Chuẩn hóa k luôn dương để phép modulo đồng nhất
    k = abs(k)
    
    for x in arr:
        current_prefix_sum += x
        remainder = current_prefix_sum % k
        
        # Nếu số dư này đã xuất hiện trước đó, cộng số lần xuất hiện vào kết quả
        if remainder in remainder_counts:
            total_count += remainder_counts[remainder]
            remainder_counts[remainder] += 1
        else:
            remainder_counts[remainder] = 1
            
    return total_count

def generate_input(test_idx):
    """Sinh dữ liệu đầu vào theo subtask"""
    if test_idx <= 3: # Dễ
        n = random.randint(10, 1000)
        k = random.randint(2, 1000)
        v_range = 10**3
    elif test_idx <= 7: # Trung bình
        n = random.randint(10001, 50000)
        k = random.randint(2, 50000)
        v_range = 10**6
    else: # Khó/Lớn
        n = 10**5
        k = random.randint(50000, 100000)
        v_range = 10**9

    # Tạo mảng
    if test_idx == 8: # Trường hợp đặc biệt: Toàn số 0
        arr = [0] * n
    elif test_idx == 9: # Trường hợp đặc biệt: Toàn số âm
        arr = [random.randint(-v_range, -1) for _ in range(n)]
    else:
        arr = [random.randint(-v_range, v_range) for _ in range(n)]
        
    return n, k, arr

def create_tests():
    # Xóa và tạo mới thư mục bài tập
    if os.path.exists(PROB_NAME):
        shutil.rmtree(PROB_NAME)
    os.makedirs(PROB_NAME)

    for i in range(1, TOTAL_TESTS + 1):
        # Tạo thư mục test001, test002...
        test_dir = os.path.join(PROB_NAME, f"test{i:03d}")
        os.makedirs(test_dir)

        # Sinh input
        n, k, arr = generate_input(i)
        
        # Ghi file .INP
        inp_path = os.path.join(test_dir, f"{PROB_NAME}.INP")
        with open(inp_path, 'w') as f:
            f.write(f"{n} {k}\n")
            f.write(" ".join(map(str, arr)) + "\n")

        # Giải chuẩn và ghi file .OUT
        ans = solve(n, k, arr)
        out_path = os.path.join(test_dir, f"{PROB_NAME}.OUT")
        with open(out_path, 'w') as f:
            f.write(str(ans) + "\n")

        print(f"Done test{i:03d}: N={n}, K={k}")

if __name__ == "__main__":
    create_tests()
    print("--- Hoàn thành tạo 10 bộ test cho bài DIVISIBLE ---")