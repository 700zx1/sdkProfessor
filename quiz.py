import random

def generate_quiz(code):
    lines = [line.strip() for line in code.splitlines() if line.strip()]
    if not lines:
        return []

    question_line = random.choice(lines)
    correct_answer = question_line.strip()
    distractors = ["print('Hello')", "x = 5", "if True:", "def foo():"]
    options = random.sample([correct_answer] + distractors, 4)

    return [{
        "question": f"What does this line do?\n\n{question_line}\n",
        "options": options,
        "answer": correct_answer
    }]
