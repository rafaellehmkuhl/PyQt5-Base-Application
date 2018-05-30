from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QPushButton, QSlider)

import numpy as np


class MyClass(QWidget):
    """Class example"""

    def __init__(parent=None):
        super().__init__()