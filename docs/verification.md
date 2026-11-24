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

## Tái lập kết quả thực nghiệm trong báo cáo

### Môi trường đã dùng

Kết quả trong báo cáo được chạy trên Windows với các phiên bản sau (đầy đủ trong `results/environment.txt`):

| Thành phần | Phiên bản |
|---|---|
| Python | 3.13.0 |
| pygame-ce | 2.5.8 |
| numpy | 2.2.3 |
| scikit-learn | 1.7.2 |
| scipy | 1.15.2 |
| joblib | 1.5.2 |

Để tái lập chính xác kết quả học máy, nên cài đúng các phiên bản trên:

```bash
pip install pygame-ce==2.5.8 numpy==2.2.3 scikit-learn==1.7.2 scipy==1.15.2 joblib==1.5.2
```

### Các yếu tố cố định

- Ba bản đồ mẫu được vẽ sẵn trong `src/robot_ai/domain/environment.py`, cùng điểm xuất phát S = (0, 0) và đích G = (10, 14).
- Dữ liệu huấn luyện sinh từ 120 bản đồ ngẫu nhiên với `seed=7`.
- Chia tập huấn luyện/kiểm tra và Random Forest dùng `random_state=1`.
- Các thuật toán tìm kiếm không dùng số ngẫu nhiên khi chạy.

### Các lệnh chạy lại

Chạy từ thư mục gốc của dự án:

```bash
python scripts/train_model.py
python scripts/run_experiments.py --ml
```

Lệnh thứ nhất huấn luyện lại mô hình và in kết quả đánh giá. Lệnh thứ hai chạy 3 bản đồ × 4 cấu hình và ghi `results/results.csv`.

### Kết quả mong đợi

**Mô hình học máy** (tập kiểm tra 3.619 mẫu, 25% của 14.475 mẫu):

| Lớp | Precision | Recall | F1 | Số mẫu |
|---|---:|---:|---:|---:|
| Thấp (0) | 0,93 | 0,74 | 0,83 | 3.165 |
| Cao (1) | 0,25 | 0,61 | 0,36 | 454 |
| Độ chính xác | | | 0,73 | 3.619 |

Mô hình cơ sở (luôn đoán lớp phổ biến nhất) đạt 0,87.

**Thực nghiệm trên ba bản đồ mẫu:**

| Bản đồ | Thuật toán | Số bước | Tối ưu | Ô đã đi | Ô quan sát | Tỷ lệ khám phá |
|---|---|---:|---:|---:|---:|---:|
| 1 | Weighted A* | 24 | 24 | 25 | 68 | 41% |
| 1 | Weighted A* + ML | 24 | 24 | 25 | 69 | 42% |
| 1 | LRTA* | 24 | 24 | 25 | 48 | 29% |
| 1 | LRTA* + ML | 24 | 24 | 25 | 48 | 29% |
| 2 | Weighted A* | 94 | 42 | 69 | 132 | 80% |
| 2 | Weighted A* + ML | 94 | 42 | 69 | 132 | 80% |
| 2 | LRTA* | 122 | 42 | 71 | 132 | 80% |
| 2 | LRTA* + ML | 116 | 42 | 71 | 132 | 80% |
| 3 | Weighted A* | 84 | 68 | 77 | 149 | 90% |
| 3 | Weighted A* + ML | 84 | 68 | 77 | 149 | 90% |
| 3 | LRTA* | 184 | 68 | 89 | 159 | 96% |
| 3 | LRTA* + ML | 240 | 68 | 89 | 159 | 96% |

Số bước, số ô và các chỉ số học máy lặp lại chính xác khi dùng cùng phiên bản thư viện. Thời gian xử lý (cột `time_ms` trong `results.csv`) phụ thuộc vào máy chạy nên chỉ nên so sánh theo bậc độ lớn.

### Các file kết quả lưu sẵn

| File | Nội dung |
|---|---|
| `results/results.csv` | Kết quả 12 cấu hình. Thời gian xử lý trong file là của lần chạy lưu sẵn, có thể khác thời gian trong báo cáo vì đo ở lần chạy khác |
| `results/ml_metrics.txt` | Kết quả huấn luyện và đánh giá mô hình |
| `results/experiments_output.txt` | Bảng kết quả in ra màn hình |
| `results/environment.txt` | Phiên bản Python và thư viện |
