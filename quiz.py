import random
import ast

def generate_distractors(code_line):
    """Generate distractors that are similar to the code line but incorrect"""
    try:
        tree = ast.parse(code_line)
        node = tree.body[0]
        
        # Generate distractors based on the node type
        if isinstance(node, ast.Assign):
            return ["x = 'Hello'", "y = 42", "result = None"]
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return ["print('World')", "print(42)", "print(None)"]
        elif isinstance(node, ast.If):
            return ["if False:", "if x > 0:", "if True:"]
        elif isinstance(node, ast.FunctionDef):
            return ["def bar():", "def baz():", "def qux():"]
        else:
            return ["print('Hello')", "x = 5", "if True:"]
    except:
        return ["print('Hello')", "x = 5", "if True:"]

def generate_quiz(code):
    try:
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        if not lines:
            return []

        # Select a random line that's not a comment or empty
        valid_lines = [line for line in lines if not line.startswith('#')]
        if not valid_lines:
            return []

        question_line = random.choice(valid_lines)
        correct_answer = question_line.strip()
        
        # Generate dynamic distractors
        distractors = generate_distractors(question_line)
        options = random.sample([correct_answer] + distractors, 4)

        return [{
            "question": f"What does this line do?\n\n{question_line}\n",
            "options": options,
            "answer": correct_answer
        }]
    except Exception as e:
        print(f"Error generating quiz: {str(e)}")
        return []


