import sys
from parser import extract_code_sections
from explain import generate_explanations
from tts_engine import speak_text
from quiz import generate_quiz

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_code_file>")
        sys.exit(1)

    try:
        code_sections = extract_code_sections(sys.argv[1])
        if not code_sections:
            print("No code sections found in the file.")
            return

        for idx, section in enumerate(code_sections, 1):
            print(f"\n--- Section {idx} ---\n")
            try:
                explanation = generate_explanations(section)
                print("Explanation:\n", explanation)
                speak_text(explanation)

                quiz = generate_quiz(section)
                if quiz:
                    for q in quiz:
                        print("\nQuiz:", q["question"])
                        for i, opt in enumerate(q["options"]):
                            print(f"  {i + 1}. {opt}")
                        try:
                            user_input = int(input("Your answer (number): ")) - 1
                            if 0 <= user_input < len(q["options"]):
                                if q["options"][user_input] == q["answer"]:
                                    print("Correct!\n")
                                else:
                                    print(f"Incorrect. Correct answer: {q['answer']}\n")
                            else:
                                print(f"Invalid option number. Correct answer: {q['answer']}\n")
                        except ValueError:
                            print(f"Please enter a number. Correct answer: {q['answer']}\n")
            except Exception as e:
                print(f"Error processing section {idx}: {str(e)}")

    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()