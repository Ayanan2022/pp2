import os

def test_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory portion: {os.path.dirname(path)}")
        print(f"Filename portion: {os.path.basename(path)}")
    else:
        print("The specified path does not exist.")

path = input("Enter a path to check: ")
test_path(path)