# Báo cáo kiểm thử

Môi trường kiểm thử của phiên làm việc:

- 7 kiểm thử tự động: đạt.
- Biên dịch cú pháp toàn bộ `src`, `scripts`, `tests` bằng `compileall`: đạt.
- Chạy CLI thực nghiệm: đạt.
- Chạy đủ 6 cấu hình (3 bản đồ × 2 thuật toán): cả 6 đều đến đích.

| Bản đồ | Weighted A* | LRTA* |
|---|---:|---:|
| 1 | 24 bước | 24 bước |
| 2 | 94 bước | 122 bước |
| 3 | 84 bước | 184 bước |

Lưu ý: không thể kiểm tra hiển thị cửa sổ Pygame trong môi trường đóng gói này vì môi trường kiểm thử không cài module `pygame`. Trên máy Windows, cài dependencies bằng `pip install -r requirements.txt`, sau đó chạy `python scripts/run.py` để kiểm tra giao diện thực tế.
