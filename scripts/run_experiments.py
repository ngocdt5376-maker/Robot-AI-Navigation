"""Chạy bộ thực nghiệm từ dòng lệnh."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from robot_ai.application.experiments import main

if __name__ == "__main__":
    main()
