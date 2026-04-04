# Viết script sinh test tại đây
import os
import random
import shutil

# Cấu hình bài toán
PROB_NAME = "SUMK"
TOTAL_TESTS = 10

def solve(n, k, arr):
    """Sử dụng Prefix Sum + Hash Map để tìm dãy con đầu tiên có tổng bằng K"""
    prefix_map = {0: -1} # Để xử lý trường hợp dãy con bắt đầu từ chỉ số 0
    current_sum = 0
    for idx, val in enumerate(arr):
        current_sum += val
        target = current_sum - k
        if target in prefix_map:
            return f"{prefix_map[target] + 1} {idx}"
        # Chỉ lưu lần xuất hiện đầu tiên của mỗi prefix_sum để đảm bảo dãy con sớm nhất
        if current_sum not in prefix_map:
            prefix_map[current_sum] = idx
    return "-1"

def generate_input(test_idx):
    """Sinh dữ liệu đầu vào cho từng loại test"""
    if test_idx <= 3: # Test dễ
        n = random.randint(10, 1000)
        k = random.randint(-2000, 2000)
        arr = [random.randint(-500, 500) for _ in range(n)]
    elif test_idx <= 7: # Test trung bình
        n = random.randint(1001, 100000)
        k = random.randint(-10**9, 10**9)
        arr = [random.randint(-10**6, 10**6) for _ in range(n)]
    else: # Test khó/lớn
        n = 10**6
        k = random.randint(-10**9, 10**9)
        arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    # Case đặc biệt: Đảm bảo có ít nhất 2 test có kết quả -1
    if test_idx == 5 or test_idx == 10:
        k = 2 * 10**15 # Số cực lớn để không thể có tổng bằng K
        
    # Case đặc biệt: Tổng K nằm ở ngay đầu hoặc ngay cuối
    if test_idx == 1:
        arr[0] = k
    if test_idx == 9:
        arr[-1] = k
        
    return n, k, arr

def create_tests():
    # Khởi tạo thư mục bài tập
    if os.path.exists(PROB_NAME):
        shutil.rmtree(PROB_NAME)
    os.makedirs(PROB_NAME)

    for i in range(1, TOTAL_TESTS + 1):
        # Tạo thư mục test
        test_dir = os.path.join(PROB_NAME, f"test{i:03d}")
        os.makedirs(test_dir)

        # Sinh dữ liệu
        n, k, arr = generate_input(i)
        
        # Ghi file INP
        inp_path = os.path.join(test_dir, f"{PROB_NAME}.INP")
        with open(inp_path, 'w') as f:
            f.write(f"{n} {k}\n")
            f.write(" ".join(map(str, arr)) + "\n")

        # Giải bài và ghi file OUT
        ans = solve(n, k, arr)
        out_path = os.path.join(test_dir, f"{PROB_NAME}.OUT")
        with open(out_path, 'w') as f:
            f.write(str(ans) + "\n")

        print(f"Successfully created test{i:03d} (N={n})")

if __name__ == "__main__":
    create_tests()
    print("--- Hoàn tất sinh 10 bộ test ---")