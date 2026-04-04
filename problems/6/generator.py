import os
import random
import shutil

# Cấu hình bài toán
PROB_NAME = "MAXSUB"
TOTAL_TESTS = 10

def solve(n, arr):
    """Thuật toán Kadane tối ưu O(N)"""
    max_so_far = 0
    current_max = 0
    for x in arr:
        current_max += x
        if current_max < 0:
            current_max = 0
        if max_so_far < current_max:
            max_so_far = current_max
    return max_so_far

def generate_input(subtask, test_idx):
    """Sinh dữ liệu đầu vào dựa trên subtask"""
    if subtask == 1:
        n = random.randint(1, 1000)
        v_min, v_max = -1000, 1000
    elif subtask == 2:
        n = random.randint(1001, 100000)
        v_min, v_max = -10**6, 10**6
    else:
        # Subtask 3: N lên đến 10^6
        n = random.randint(500000, 1000000)
        v_min, v_max = -10**6, 10**6

    # Các trường hợp đặc biệt
    if test_idx == 1: # Test toàn âm
        arr = [random.randint(-1000, -1) for _ in range(n)]
    elif test_idx == 2: # Test toàn dương
        arr = [random.randint(1, 1000) for _ in range(n)]
    else:
        arr = [random.randint(v_min, v_max) for _ in range(n)]
    
    return n, arr

def create_tests():
    # Xóa thư mục cũ nếu có
    if os.path.exists(PROB_NAME):
        shutil.rmtree(PROB_NAME)
    os.makedirs(PROB_NAME)

    for i in range(1, TOTAL_TESTS + 1):
        # Xác định subtask
        if i <= 3:
            subtask = 1
        elif i <= 6:
            subtask = 2
        else:
            subtask = 3

        # Tạo thư mục test
        test_dir = os.path.join(PROB_NAME, f"test{i:03d}")
        os.makedirs(test_dir)

        # Sinh input
        n, arr = generate_input(subtask, i)
        
        inp_path = os.path.join(test_dir, f"{PROB_NAME}.INP")
        with open(inp_path, 'w') as f:
            f.write(f"{n}\n")
            f.write(" ".join(map(str, arr)) + "\n")

        # Giải bài tạo output
        ans = solve(n, arr)
        out_path = os.path.join(test_dir, f"{PROB_NAME}.OUT")
        with open(out_path, 'w') as f:
            f.write(str(ans) + "\n")

        print(f"Created {test_dir} (Subtask {subtask}, N={n})")

if __name__ == "__main__":
    create_tests()
    print("--- Done! ---")