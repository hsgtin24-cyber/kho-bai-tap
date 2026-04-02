import os
import random
import shutil

# Cấu hình bài toán
TEN_BAI = "UNIQUE"
SO_TEST = 10

def solve(n, a):
    """Lời giải chuẩn: Đếm số lượng phần tử khác nhau trong dãy đã sắp xếp"""
    if n == 0:
        return 0
    cnt = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            cnt += 1
    return cnt

def generate_input(subtask):
    if subtask == 1: # Dễ
        n = random.randint(1, 1000)
        max_val = 100
    elif subtask == 2: # Trung bình
        n = random.randint(1001, 10**5)
        max_val = 10**6
    else: # Khó
        n = random.randint(10**5, 10**6)
        max_val = 10**9

    # Sinh dãy tăng dần
    a = []
    curr = random.randint(-max_val, 0)
    for _ in range(n):
        # Tỉ lệ xuất hiện số trùng cao để test tính "làm sạch"
        step = random.choices([0, random.randint(1, 100)], weights=[70, 30])[0]
        curr += step
        if curr > 10**9: curr = 10**9
        a.append(curr)
    
    # Đảm bảo dãy luôn được sort (phòng trường hợp step âm hoặc logic lỗi)
    a.sort()
    return n, a

def make_test(test_num, subtask):
    path = f"{TEN_BAI}/test{test_num:03d}"
    if not os.path.exists(path):
        os.makedirs(path)

    # Biên và Edge cases
    if test_num == 1:
        n, a = 1, [100]
    elif test_num == 2:
        n = 10
        a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] # Giống ví dụ
    else:
        n, a = generate_input(subtask)

    # Ghi file INP
    inp_path = os.path.join(path, f"{TEN_BAI}.INP")
    with open(inp_path, 'w') as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, a)) + "\n")

    # Giải và ghi file OUT
    ans = solve(n, a)
    out_path = os.path.join(path, f"{TEN_BAI}.OUT")
    with open(out_path, 'w') as f:
        f.write(str(ans))

def main():
    if os.path.exists(TEN_BAI):
        shutil.rmtree(TEN_BAI)
    
    # Phân bổ: 3 test dễ (1-3), 4 test trung bình (4-7), 3 test khó (8-10)
    for i in range(1, SO_TEST + 1):
        if i <= 3:
            sub = 1
        elif i <= 7:
            sub = 2
        else:
            sub = 3
        make_test(i, sub)
        print(f"Generated test {i:03d}")

if __name__ == "__main__":
    main()