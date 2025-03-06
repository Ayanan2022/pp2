def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")

file_path = input("Enter file path: ")
count_lines(file_path)