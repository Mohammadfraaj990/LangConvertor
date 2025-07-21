from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QVBoxLayout, QLabel, QPushButton, QComboBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys, os

# Ensure import path is correct
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from converter.convert import convert_code


class LangConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Code Language Converter")
        self.setGeometry(200, 200, 900, 700)
        self.setStyleSheet("background-color: #101820; color: #ffffff;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("\U0001F4A1 Convert Code Between Languages")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.code_input = QTextEdit()
        self.code_input.setPlaceholderText("Paste your code here...")
        self.code_input.setFont(QFont("Consolas", 12))

        self.from_lang = QComboBox()
        self.from_lang.addItems(["Python", "Java", "C++", "JavaScript"])
        self.from_lang.setFont(QFont("Segoe UI", 11))

        self.to_lang = QComboBox()
        self.to_lang.addItems(["Java", "Python", "C++", "JavaScript"])
        self.to_lang.setFont(QFont("Segoe UI", 11))

        self.convert_btn = QPushButton("\u27a1\ufe0f Convert")
        self.convert_btn.setFont(QFont("Segoe UI", 12))
        self.convert_btn.setStyleSheet("background-color: #00adb5; color: black; padding: 8px; border-radius: 8px;")
        self.convert_btn.clicked.connect(self.convert_code_action)

        self.result = QTextEdit()
        self.result.setReadOnly(True)
        self.result.setFont(QFont("Consolas", 12))
        self.result.setStyleSheet("background-color: #1a1a1a; color: #00ffcc;")

        layout.addWidget(title)
        layout.addWidget(QLabel("From:"))
        layout.addWidget(self.from_lang)
        layout.addWidget(QLabel("To:"))
        layout.addWidget(self.to_lang)
        layout.addWidget(QLabel("Your Code:"))
        layout.addWidget(self.code_input)
        layout.addWidget(self.convert_btn)
        layout.addWidget(QLabel("Converted Output:"))
        layout.addWidget(self.result)

        self.setLayout(layout)

    def convert_code_action(self):
        code = self.code_input.toPlainText().strip()
        source_lang = self.from_lang.currentText()
        target_lang = self.to_lang.currentText()

        if not code:
            self.result.setText("Please enter some code to convert.")
            return

        self.result.setText("\u23f3 Converting...")
        converted = convert_code(code, source_lang, target_lang)
        self.result.setText(converted)
