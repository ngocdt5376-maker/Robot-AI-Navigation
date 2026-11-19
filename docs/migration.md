# Ánh xạ từ phiên bản ZIP ban đầu

| Module ban đầu | Module sau tái cấu trúc |
|---|---|
| `environment.py` | `src/robot_ai/domain/environment.py` |
| `robot.py` | `src/robot_ai/domain/robot.py` |
| `algorithms.py` | `src/robot_ai/algorithms/search.py` |
| `simulation.py` | `src/robot_ai/application/simulation.py` |
| `ml_model.py` | `src/robot_ai/machine_learning/model.py` |
| `ui.py` | `src/robot_ai/presentation/ui.py` |
| `experiments.py` | `src/robot_ai/application/experiments.py` |
| `main.py` | `src/robot_ai/main.py` |

Các thuật toán và phần xử lý cốt lõi được giữ lại; thay đổi chính là vị trí module và import package. Kết quả thực nghiệm được chuẩn hóa vào `results/results.csv`.
