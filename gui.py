import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
)
from parser import extract_code_sections
from explain import generate_explanations
from tts_engine import speak_text
from quiz import generate_quiz

class SDKProfessorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sdkProfessor")
        self.setGeometry(300, 300, 800, 600)

        self.layout = QVBoxLayout()

        self.explain_output = QTextEdit()
        self.explain_output.setReadOnly(True)

        self.quiz_output = QTextEdit()
        self.quiz_output.setReadOnly(True)

        self.load_button = QPushButton("Open Python File")
        self.load_button.clicked.connect(self.load_code)

        self.layout.addWidget(QLabel("Explanation:"))
        self.layout.addWidget(self.explain_output)
        self.layout.addWidget(QLabel("Quiz:"))
        self.layout.addWidget(self.quiz_output)
        self.layout.addWidget(self.load_button)
        self.setLayout(self.layout)

    def load_code(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Python File", "", "Python Files (*.py)")
        if file_path:
            self.explain_output.clear()
            self.quiz_output.clear()
            sections = extract_code_sections(file_path)
            for section in sections:
                explanation = generate_explanations(section)
                self.explain_output.append(explanation)
                speak_text(explanation)

                quiz = generate_quiz(section)
                for q in quiz:
                    self.quiz_output.append(q["question"])
                    for opt in q["options"]:
                        self.quiz_output.append(f" - {opt}")
                    self.quiz_output.append("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SDKProfessorApp()
    window.show()
    sys.exit(app.exec())
