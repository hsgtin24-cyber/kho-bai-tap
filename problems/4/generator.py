# Viết script sinh test tại đây
import os
import random
import shutil

TEN_BAI = "BRICKS"

def solve(n, a, b):
    # Công thức tổng cấp số cộng: n/2 * (2a + (n-1)b)
    # Viết dưới dạng (n * (2*a + (n-1)*b)) // 2 để tránh sai số số thực
    total = (n * (2 * a + (n - 1) * b)) // 2
    return total

def make_test(test_num, n, a, b):
    folder = f"{TEN_BAI}/test{test_num:03d}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Ghi file INP
    inp_path = os.path.join(folder, f"{TEN_BAI}.INP")
    with open(inp_path, "w") as f:
        f.write(f"{n} {a} {b}")
        
    # Ghi file OUT
    out_path = os.path.join(folder, f"{TEN_BAI}.OUT")
    result = solve(n, a, b)
    with open(out_path, "w") as f:
        f.write(str(result))

def main():
    # Xóa thư mục cũ nếu có
    if os.path.exists(TEN_BAI):
        shutil.rmtree(TEN_BAI)
    
    # Test 001: Ví dụ trong đề
    make_test(1, 5, 1, 1)
    
    # Subtask 1: N, A, B nhỏ (Test 2-3)
    make_test(2, 10, 2, 3)
    make_test(3, 100, 1, 1)
    
    # Subtask 2: N, A, B trung bình (Test 4-7)
    for i in range(4, 8):
        n = random.randint(10**5, 10**6)
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**3)
        make_test(i, n, a, b)
        
    # Subtask 3: N, A, B lớn (Test 8-10)
    # Test 8: N cực lớn
    make_test(8, 10**9, 1, 1)
    # Test 9: A, B cực lớn
    make_test(9, 10**6, 10**9, 10**9)
    # Test 10: Tất cả đều cực lớn (Max giới hạn)
    make_test(10, 10**9, 10**9, 10**9)

    print(f"Đã tạo thành công 10 test cho bài {TEN_BAI}")

if __name__ == "__main__":
    main()