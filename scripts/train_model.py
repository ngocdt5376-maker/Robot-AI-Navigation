"""Huấn luyện và đánh giá mô hình Random Forest."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from robot_ai.machine_learning.model import MachineLearningModel

if __name__ == "__main__":
    MachineLearningModel().train()
