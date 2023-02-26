"""
Pulled from Zeta36/chess-alpha-zero
"""

import os
import sys
import multiprocessing as mp
from src_code.a_config.config import make_chess_config
from src_code.b_manager.manager import start


def control():
    az = make_chess_config()
    start('')


if __name__ == "__main__":
    control()
