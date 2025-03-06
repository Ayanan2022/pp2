import os

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File {file_path} deleted.")
    else:
        print("File does not exist or no write permission.")

file_path = input("Enter file path to delete: ")
delete_file(file_path)