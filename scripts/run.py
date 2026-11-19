"""Khởi chạy ứng dụng Pygame."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from robot_ai.main import main

if __name__ == "__main__":
    main()
