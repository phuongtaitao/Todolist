# ỨNG DỤNG TO-DO LIST PRO (QUẢN TRỊ KHOA HỌC & LOGIC)

Ứng dụng quản lý công việc và dự án cá nhân được thiết kế chuyên biệt để chạy trực tiếp trên máy tính Windows, đáp ứng đầy đủ yêu cầu:
- **Nhiều Mini Project trong 1 danh sách**: Mỗi mini project là một nhóm mục tiêu riêng biệt, có mã quản lý (`PRJ-01`, `PRJ-02`), biểu tượng, và thanh tiến độ hoàn thành (%).
- **Quản lý công việc phát sinh khoa học**: Phân định rõ giữa `📋 Kế hoạch gốc (Planned)` và `⚡ Việc mới phát sinh (Emergent)` để kiểm soát khối lượng công việc đột xuất.
- **Thuật toán chống trùng lặp (Anti-duplicate)**: Tự động phát hiện và cảnh báo ngay lập tức nếu bạn nhập công việc có tên trùng hoặc tương tự (tránh ghi đè hoặc tạo thừa).
- **Phân rã việc con (Subtasks)**: Mỗi công việc lớn có thể chia thành danh sách checklist các bước nhỏ.
- **Tự động lưu vĩnh viễn trên máy tính**: Dữ liệu lưu trong cơ sở dữ liệu SQLite (`data/todo_app.db`), không bao giờ bị mất khi tắt máy.

---

## 🚀 HƯỚNG DẪN KHỞI CHẠY

Bạn có 2 lựa chọn cực kỳ thuận tiện để sử dụng ngay:

### Lựa chọn 1: Dùng ngay tức thì (Không cần cài đặt gì thêm)
- Trong thư mục này, click đúp chuột vào file:
  👉 **`todo_offline.html`**
- Ứng dụng sẽ mở ngay lập tức trên trình duyệt (Microsoft Edge, Chrome, Cốc Cốc...) với giao diện hiện đại, đầy đủ mọi tính năng: Mini Project, việc phát sinh, chống trùng lặp, lưu dữ liệu cục bộ trên máy.

---

### Lựa chọn 2: Chạy phiên bản Desktop Python
- Click đúp vào file:
  👉 **`chay_ung_dung.bat`** (hoặc `run.bat`)

> **Lưu ý nếu máy tính bạn chưa cài Python:**
> 1. Khi bạn click đúp vào `chay_ung_dung.bat`, chương trình sẽ tự kiểm tra. Nếu chưa có Python, màn hình sẽ thông báo và tự động mở trang web tải Python chính thức: [python.org/downloads](https://www.python.org/downloads/).
> 2. Bạn chỉ cần tải file cài đặt Python về và mở lên.
> 3. **CỰC KỲ QUAN TRỌNG**: Ở màn hình cài đặt đầu tiên, hãy **tích chọn vào ô: `[x] Add python.exe to PATH`** (ở góc dưới cùng), sau đó nhấn **Install Now**.
> 4. Cài xong, bạn chỉ việc click đúp lại vào `chay_ung_dung.bat` để tận hưởng ứng dụng cửa sổ Desktop!

---

## 📂 CẤU TRÚC THƯ MỤC DỰ ÁN

```text
d:\My Pyton\Máng AI\
├── main.py                  # Điểm khởi chạy ứng dụng Desktop Python
├── chay_ung_dung.bat        # File click đúp khởi động ứng dụng (1 click)
├── run.bat                  # File khởi động phụ
├── todo_offline.html        # Phiên bản Web Offline mở ngay lập tức
├── README.md                # Tài liệu hướng dẫn sử dụng
│
├── app/
│   ├── database.py          # Quản lý SQLite: Bảng projects, tasks, subtasks, logs
│   ├── ui/
│   │   ├── theme.py         # Bảng màu Indigo/Slate, font chữ Segoe UI
│   │   ├── main_window.py   # Cửa sổ chính, thanh tìm kiếm và thêm nhanh
│   │   ├── sidebar.py       # Cột Mini Projects và các bộ lọc nhanh
│   │   ├── task_list.py     # Thẻ hiển thị công việc (Task Cards) & thao tác
│   │   ├── task_dialog.py   # Modal thêm/sửa chi tiết + cảnh báo trùng lặp
│   │   ├── project_dialog.py# Modal tạo/sửa Mini Project
│   │   └── stats_dialog.py  # Báo cáo thống kê tiến độ khoa học
│   └── utils/
│       ├── helpers.py       # Thuật toán đối chiếu văn bản, tính hạn chót
│       └── export_import.py # Sao lưu & phục hồi dữ liệu qua file JSON
│
└── data/
    └── todo_app.db          # Cơ sở dữ liệu SQLite tự động tạo
```

---

## 🌟 CÁC TÍNH NĂNG NỔI BẬT ĐƯỢC THIẾT KẾ RIÊNG

1. **Thanh thêm nhanh (Quick-Add)**:
   - Gõ tiêu đề việc, chọn nhanh mức ưu tiên (Cao / Vừa / Thấp) và chọn loại (`📋 Kế hoạch` hoặc `⚡ Phát sinh`), nhấn **Enter** là việc được thêm ngay.
2. **Cảnh báo trùng lặp thông minh**:
   - Khi bạn gõ tên công việc, ứng dụng sẽ so khớp với tất cả các công việc hiện có. Nếu có việc tương đồng (ví dụ: đã có "Báo cáo doanh thu tháng 10" mà bạn lại gõ "Báo cáo doanh thu t10"), hệ thống sẽ hiển thị cảnh báo đỏ ngay trên màn hình.
3. **Quản lý Deadline trực quan**:
   - Tự động đánh dấu màu đỏ kèm số ngày trễ với những việc **Quá hạn**.
   - Đánh dấu màu cam nổi bật với những việc có hạn **Hôm nay**.
4. **Báo cáo phân tích khoa học**:
   - Bấm nút **📊 Phân tích & Báo cáo** ở góc dưới bên trái để xem: Tỉ lệ hoàn thành, Tỉ trọng việc phát sinh vs Kế hoạch, cùng các gợi ý quản trị thời gian.
5. **Sao lưu an toàn**:
   - Nút **💾 Sao lưu** và **📂 Khôi phục** cho phép bạn xuất toàn bộ dữ liệu ra file `.json` để lưu giữ hoặc chuyển sang máy tính khác khi cần.
