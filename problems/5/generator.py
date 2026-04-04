# Viết script sinh test tại đây
import os
import random
import shutil

# --- Cấu hình bài toán ---
PROBLEM_NAME = "COLORS"
TOTAL_TESTS = 10

def solve(n, m, a):
    """Lời giải chuẩn sử dụng Two Pointers"""
    if m == 0: return 0
    cnt = {}
    distinct_count = 0
    left = 0
    min_len = float('inf')
    
    for right in range(n):
        color = a[right]
        cnt[color] = cnt.get(color, 0) + 1
        if cnt[color] == 1:
            distinct_count += 1
            
        while distinct_count == m:
            min_len = min(min_len, right - left + 1)
            left_color = a[left]
            cnt[left_color] -= 1
            if cnt[left_color] == 0:
                distinct_count -= 1
            left += 1
            
    return min_len if min_len != float('inf') else 0

def generate_input(n_max, m_max, case_type="random"):
    """Sinh dữ liệu input dựa trên loại test"""
    if case_type == "no_solution":
        n = n_max
        m = m_max
        # Chỉ sinh tối đa m-1 màu để không bao giờ đủ m màu
        a = [random.randint(1, m-1) for _ in range(n)]
    elif case_type == "edge_min":
        n = m_max
        m = m_max
        a = list(range(1, m + 1))
        random.shuffle(a)
    else:
        n = n_max
        m = m_max
        a = [random.randint(1, m) for _ in range(n)]
        
    return n, m, a

def create_tests():
    if os.path.exists(PROBLEM_NAME):
        shutil.rmtree(PROBLEM_NAME)
    os.makedirs(PROBLEM_NAME)

    for i in range(1, TOTAL_TESTS + 1):
        test_dir = os.path.join(PROBLEM_NAME, f"test{i:03d}")
        os.makedirs(test_dir)
        
        # Thiết lập giới hạn N, M theo subtask
        if i <= 3: # Subtask 1: N <= 100
            n_val = random.randint(10, 100)
            m_val = random.randint(2, min(n_val, 50))
        elif i <= 6: # Subtask 2: N <= 1000
            n_val = random.randint(500, 1000)
            m_val = random.randint(10, 200)
        else: # Subtask 3: N <= 10^5
            n_val = random.randint(80000, 100000)
            m_val = random.randint(100, n_val // 2)

        # Điều chỉnh đặc biệt cho một số test case
        case_type = "random"
        if i == 1: case_type = "edge_min"
        if i == 7: case_type = "no_solution"

        n, m, a = generate_input(n_val, m_val, case_type)
        
        # Ghi file INP
        inp_path = os.path.join(test_dir, f"{PROBLEM_NAME}.INP")
        with open(inp_path, "w") as f:
            f.write(f"{n} {m}\n")
            f.write(" ".join(map(str, a)) + "\n")
            
        # Giải và ghi file OUT
        ans = solve(n, m, a)
        out_path = os.path.join(test_dir, f"{PROBLEM_NAME}.OUT")
        with open(out_path, "w") as f:
            f.write(str(ans) + "\n")

    print(f"Đã sinh thành công {TOTAL_TESTS} test trong thư mục '{PROBLEM_NAME}'")

if __name__ == "__main__":
    create_tests()
