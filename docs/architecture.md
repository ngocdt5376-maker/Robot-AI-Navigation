# Kiến trúc hệ thống

Dự án được tổ chức theo các nhóm trách nhiệm để giảm phụ thuộc chéo và giúp kiểm thử dễ hơn.

1. **Domain** (`domain/`): `Environment` quản lý bản đồ thật và quan sát; `Robot` lưu vị trí, tri thức đã quan sát, lịch sử và trạng thái.
2. **Algorithms** (`algorithms/`): Weighted A*, LRTA*, tìm kiếm BFS phụ trợ và lựa chọn vùng biên khám phá.
3. **Application** (`application/`): `Simulation` điều phối chu trình quan sát → quyết định → kiểm tra → di chuyển; `experiments` chạy các cấu hình.
4. **Machine learning** (`machine_learning/`): tạo dữ liệu, huấn luyện/đọc Random Forest và dự đoán rủi ro.
5. **Presentation** (`presentation/`): Pygame chỉ xử lý hiển thị và sự kiện người dùng.
6. **Entry point** (`main.py`): kết nối giao diện với lớp ứng dụng.

Luồng phụ thuộc chính: Presentation → Application → Domain/Algorithms; Application có thể sử dụng Machine Learning thông qua hàm dự đoán rủi ro.
