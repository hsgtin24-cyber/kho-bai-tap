# Viết script sinh test tại đây
import os
import random
import shutil

TEN_BAI = "PASSWORD"

def solve(s):
    n = len(s)
    ans = 0
    upper = []
    lower = []
    digit = []
    
    # Tiền xử lý vị trí các loại ký tự
    for i, char in enumerate(s):
        if 'A' <= char <= 'Z': upper.append(i)
        elif 'a' <= char <= 'z': lower.append(i)
        elif '0' <= char <= '9': digit.append(i)
        
    u_idx = l_idx = d_idx = 0
    num_u, num_l, num_d = len(upper), len(lower), len(digit)
    
    for i in range(n):
        # Tìm vị trí xuất hiện đầu tiên của mỗi loại ký tự kể từ i
        while u_idx < num_u and upper[u_idx] < i: u_idx += 1
        while l_idx < num_l and lower[l_idx] < i: l_idx += 1
        while d_idx < num_d and digit[d_idx] < i: d_idx += 1
        
        if u_idx < num_u and l_idx < num_l and d_idx < num_d:
            # Vị trí j gần nhất thỏa mãn 3 loại ký tự
            j_min_types = max(upper[u_idx], lower[l_idx], digit[d_idx])
            # Vị trí j gần nhất thỏa mãn độ dài >= 6
            j_min_len = i + 5
            
            start_j = max(j_min_types, j_min_len)
            if start_j < n:
                ans += (n - start_j)
                
    return ans

def generate_input(n, case_type="random"):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if case_type == "no_upper":
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    elif case_type == "no_digit":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif case_type == "short":
        n = random.randint(1, 5)
        
    return "".join(random.choice(chars) for _ in range(n))

def make_test(test_num, n, case_type="random"):
    folder = f"{TEN_BAI}/test{test_num:03d}"
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # Sinh Input
    s = generate_input(n, case_type)
    if test_num == 1: s = "Adsd2bfB4D" # Example case
    
    inp_path = os.path.join(folder, f"{TEN_BAI}.INP")
    with open(inp_path, "w") as f:
        f.write(s)
        
    # Sinh Output
    out_path = os.path.join(folder, f"{TEN_BAI}.OUT")
    result = solve(s)
    with open(out_path, "w") as f:
        f.write(str(result))

def main():
    if os.path.exists(TEN_BAI):
        shutil.rmtree(TEN_BAI)
    
    # Subtask 1: N <= 100 (3 test)
    make_test(1, 10) # Example
    make_test(2, 5, "short") # Biên độ dài < 6
    make_test(3, 100, "no_upper") # Thiếu loại ký tự
    
    # Subtask 2: N <= 5000 (4 test)
    for i in range(4, 8):
        make_test(i, random.randint(1000, 5000))
        
    # Subtask 3: N <= 10^6 (3 test)
    make_test(8, 10**5)
    make_test(9, 5 * 10**5)
    make_test(10, 10**6)

    print(f"Đã sinh thành công 10 test cho bài {TEN_BAI}")

if __name__ == "__main__":
    main()