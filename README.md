# Robot AI Navigation

Mô phỏng robot tự hành tìm đường và khám phá mê cung 2D bằng Python + Pygame.

## Chức năng

- 3 bản đồ mê cung mẫu; robot không biết trước toàn bộ bản đồ.
- Quan sát lân cận, cập nhật bản đồ đã biết và lịch sử di chuyển.
- Weighted A* và LRTA*; cơ chế khám phá các ô biên.
- Random Forest hỗ trợ đánh giá rủi ro (có thể chạy không có scikit-learn).
- Start, Pause, Step, Reset; chọn bản đồ/thuật toán; điều chỉnh tốc độ và trọng số.
- Giao diện sáng/tối, phím tắt, thống kê và bảng so sánh thực nghiệm.
- Xuất kết quả thực nghiệm thành `results/results.csv`.

## Cài đặt (Windows / VS Code)

```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
python scripts/run.py
```

Hoặc từ thư mục gốc sau khi cài package: `python -m robot_ai.main` (cần `src` nằm trong PYTHONPATH).

## Chạy thực nghiệm

```bash
python scripts/run_experiments.py
python scripts/run_experiments.py --ml
python scripts/run_experiments.py --weight 2.0
```

## Huấn luyện mô hình

```bash
python scripts/train_model.py
```

Mô hình sinh ra được lưu trong `models/risk_model.joblib` và không được commit lên GitHub vì có thể tái tạo.

## Phím tắt

| Phím | Chức năng |
|---|---|
| Space | Chạy / tạm dừng |
| N | Đi một bước |
| R | Reset |
| 1 / 2 / 3 | Chọn bản đồ |
| W / L | Weighted A* / LRTA* |
| M | Bật / tắt ML |
| T | Đổi giao diện sáng / tối |
| Esc | Thoát |

## Kiến trúc

- `domain`: môi trường và trạng thái robot.
- `algorithms`: thuật toán tìm kiếm và ra quyết định.
- `application`: điều phối mô phỏng và thực nghiệm.
- `machine_learning`: sinh dữ liệu, huấn luyện và dự đoán rủi ro.
- `presentation`: giao diện Pygame.
- `infrastructure`: điểm mở rộng cho lưu trữ/tài nguyên.

Chi tiết: xem `docs/architecture.md` và `docs/user_guide.md`.
