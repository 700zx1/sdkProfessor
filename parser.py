import ast

def extract_code_sections(file_path):
    with open(file_path, 'r') as file:
        source = file.read()

    tree = ast.parse(source)
    code_sections = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            start_line = node.lineno - 1
            end_line = max([getattr(n, 'lineno', start_line) for n in ast.walk(node)])
            code = "\n".join(source.splitlines()[start_line:end_line])
            code_sections.append(code)

    return code_sections
