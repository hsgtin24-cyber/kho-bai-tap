# 🏆 Olympiad Programming Library

Hệ thống quản lý bài tập và lời giải cho Đội tuyển HSG Tin học, được thiết kế tối giản, tốc độ cao và host tĩnh bằng GitHub Pages.

## Hướng dẫn thêm bài toán mới

**Bước 1: Tạo cấu trúc thư mục**
Vào thư mục `problems/`, tạo một thư mục mới có tên là `id` của bài toán (viết thường, không dấu, dùng gạch nối).
Ví dụ: `problems/dynamic-programming-tree/`

**Bước 2: Chuẩn bị nội dung**
Bên trong thư mục vừa tạo, hãy tạo các file:
- `solution.html`: Viết phân tích giải thuật và code mẫu.
- `problem.md` (Tùy chọn): Đề bài chuẩn định dạng Markdown.
- Thư mục `themis/` (Tùy chọn): Chứa file test case (in/out) để chạy qua Themis cục bộ.

**Bước 3: Khai báo Metadata**
Mở file `data/problems.json` và thêm object mới:
```json
{
  "id": "dynamic-programming-tree",
  "title": "Quy hoạch động trên cây",
  "topics": ["DP", "Graph"],
  "difficulty": 4,
  "complexity": "O(N)",
  "source": "Olympic 30/4",
  "tags": ["tree dp", "dfs"],
  "solution": "problems/dynamic-programming-tree/solution.html"
}