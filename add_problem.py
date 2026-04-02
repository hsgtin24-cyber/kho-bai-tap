import os
import json
from pathlib import Path

# Đường dẫn file
DATA_FILE = 'data/problems.json'
PROBLEMS_DIR = 'problems'

def create_boilerplate_html(title):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: system-ui, sans-serif; line-height: 1.6; color: #333; padding: 20px; }}
        pre {{ background: #f4f4f4; padding: 15px; border-radius: 8px; overflow-x: auto; }}
        code {{ font-family: "Fira Code", monospace; font-size: 14px; }}
        h2 {{ color: #2c3e50; }}
    </style>
</head>
<body>
    <h2>Phân tích bài toán {title}</h2>
    <p>Viết ý tưởng giải vào đây...</p>
    
    <h2>Code mẫu</h2>
    <pre><code>
// Viết code vào đây
    </code></pre>
</body>
</html>"""

def main():
    print("🚀 TOOL THÊM BÀI TẬP MỚI\n" + "="*30)
    
    # 1. Thu thập thông tin
    prob_id = input("ID bài toán (vd: knapsack-dp): ").strip().lower().replace(" ", "-")
    title = input("Tên bài toán: ").strip()
    topics_input = input("Chủ đề (cách nhau bởi dấu phẩy, vd: DP, Math): ").strip()
    topics = [t.strip() for t in topics_input.split(',')] if topics_input else []
    
    difficulty = input("Độ khó (1-5): ").strip()
    complexity = input("Độ phức tạp (vd: O(N log N)): ").strip()
    source = input("Nguồn bài (vd: VOI 2023): ").strip()
    
    tags_input = input("Tags (cách nhau bởi dấu phẩy, vd: bitmask, dfs): ").strip()
    tags = [t.strip().lower() for t in tags_input.split(',')] if tags_input else []
    
    judge_url = input("Link chấm Online (Enter để bỏ qua): ").strip()
    has_generator = input("Có dùng code sinh test không? (y/n): ").strip().lower() == 'y'

    # 2. Tạo thư mục và file boilerplate
    target_dir = Path(PROBLEMS_DIR) / prob_id
    target_dir.mkdir(parents=True, exist_ok=True)
    
    solution_path = target_dir / "solution.html"
    if not solution_path.exists():
        with open(solution_path, 'w', encoding='utf-8') as f:
            f.write(create_boilerplate_html(title))
        print(f"📁 Đã tạo thư mục và file: {solution_path}")

    generator_path = ""
    if has_generator:
        gen_file = target_dir / "generator.py"
        with open(gen_file, 'w', encoding='utf-8') as f:
            f.write("# Viết script sinh test tại đây\n")
        generator_path = f"{PROBLEMS_DIR}/{prob_id}/generator.py"
        print(f"📁 Đã tạo file sinh test: {gen_file}")

    # 3. Tạo Object metadata
    new_problem = {
        "id": prob_id,
        "title": title,
        "topics": topics,
        "difficulty": int(difficulty) if difficulty.isdigit() else 1,
        "complexity": complexity,
        "source": source,
        "tags": tags,
        "solution": f"{PROBLEMS_DIR}/{prob_id}/solution.html"
    }
    
    # if judge_url:
    #     new_problem["judge_url"] = judge_url
    new_problem["judge_url"] = "https://ntduong.pythonanywhere.com/"
    if has_generator:
        new_problem["generator"] = generator_path

    # 4. Cập nhật file JSON một cách an toàn
    data_path = Path(DATA_FILE)
    if data_path.exists():
        with open(data_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Kiểm tra trùng ID
    if any(p.get('id') == prob_id for p in data):
        print(f"⚠️ Lỗi: ID '{prob_id}' đã tồn tại! Vui lòng chọn ID khác.")
        return

    data.append(new_problem)

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\n✅ THÀNH CÔNG! Đã cập nhật problems.json.")
    print(f"👉 Bước tiếp theo: Mở file {solution_path} để viết giải thuật.")

if __name__ == "__main__":
    main()
