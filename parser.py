import os

def get_file_type(file_path):
    """Determine the file type based on extension"""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    # Map common extensions to language names
    file_types = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.php': 'PHP',
        '.rb': 'Ruby',
        '.go': 'Go',
        '.rs': 'Rust',
        '.ts': 'TypeScript',
        '.html': 'HTML',
        '.css': 'CSS',
        '.sql': 'SQL',
        '.sh': 'Shell Script'
    }
    
    return file_types.get(ext, 'Unknown')

def extract_code_sections(file_path):
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        code_sections = []
        current_section = []
        in_code_block = False

        # Get file type
        file_type = get_file_type(file_path)

        for line in lines:
            # Skip empty lines
            stripped_line = line.strip()
            if not stripped_line:
                continue

            # Skip comments based on file type
            if file_type == 'Python' and stripped_line.startswith('#'):
                continue
            elif file_type == 'JavaScript' and stripped_line.startswith('//'):
                continue
            elif file_type == 'Java' and (stripped_line.startswith('//') or stripped_line.startswith('/*')):
                continue
            elif file_type == 'C++' and (stripped_line.startswith('//') or stripped_line.startswith('/*')):
                continue
            elif file_type == 'C' and (stripped_line.startswith('//') or stripped_line.startswith('/*')):
                continue
            elif file_type == 'PHP' and (stripped_line.startswith('//') or stripped_line.startswith('/*')):
                continue
            elif file_type == 'Ruby' and (stripped_line.startswith('#') or stripped_line.startswith('=begin')):
                continue
            elif file_type == 'Go' and stripped_line.startswith('//'):
                continue
            elif file_type == 'Rust' and (stripped_line.startswith('//') or stripped_line.startswith('/*')):
                continue
            elif file_type == 'TypeScript' and (stripped_line.startswith('//') or stripped_line.startswith('/*')):
                continue
            elif file_type == 'SQL' and stripped_line.startswith('--'):
                continue
            elif file_type == 'Shell Script' and (stripped_line.startswith('#') or stripped_line.startswith('##')):
                continue

            # Start a new section when we encounter a non-empty line
            if not in_code_block:
                current_section = [line]
                in_code_block = True
            else:
                # Add to current section if it's indented
                if line.startswith(' ' * 4) or line.startswith('\t') or line.startswith('    '):
                    current_section.append(line)
                else:
                    # End current section and start new one
                    code_sections.append(''.join(current_section))
                    current_section = [line]

        # Add the last section if it exists
        if current_section:
            code_sections.append(''.join(current_section))

        return code_sections, file_type

    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return [], "Unknown"
