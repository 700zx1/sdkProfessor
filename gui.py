import sys
import os
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

        self.load_button = QPushButton("Open Code File")
        self.load_button.clicked.connect(self.load_code)

        self.layout.addWidget(QLabel("Explanation:"))
        self.layout.addWidget(self.explain_output)
        self.layout.addWidget(QLabel("Quiz:"))
        self.layout.addWidget(self.quiz_output)
        self.layout.addWidget(self.load_button)
        self.setLayout(self.layout)

    def load_code(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Open Code File", "", "All Files (*.*)")
            if file_path:
                self.explain_output.clear()
                self.quiz_output.clear()
                
                # Get sections and file type
                sections, file_type = extract_code_sections(file_path)
                if not sections:
                    self.explain_output.append("No code sections found in the file.")
                    return

                # Display file information
                self.explain_output.append(f"\n=== File Analysis ===\n")
                self.explain_output.append(f"File: {os.path.basename(file_path)}")
                self.explain_output.append(f"Type: {file_type}")
                self.explain_output.append("-" * 50)

                for section in sections:
                    # Generate explanation with file type context
                    prompt = f"""You are a professor teaching code to a beginner student. 
                    Explain the following {file_type} code line by line in an easy-to-understand way:
                    
                    {section}
                    """
                    
                    explanation = generate_explanations(prompt)
                    self.explain_output.append(f"\n=== Code Section ===\n")
                    self.explain_output.append(explanation)
                    speak_text(explanation)

                    # Generate quiz with file type context
                    quiz = generate_quiz(section)
                    if quiz:
                        self.quiz_output.append(f"\n=== Quiz Section ===\n")
                        for q in quiz:
                            self.quiz_output.append(f"Question: {q["question"]}")
                            for i, opt in enumerate(q["options"]):
                                self.quiz_output.append(f"  {i + 1}. {opt}")
                            self.quiz_output.append("")
        except Exception as e:
            self.explain_output.append(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SDKProfessorApp()
    window.show()
    sys.exit(app.exec())
