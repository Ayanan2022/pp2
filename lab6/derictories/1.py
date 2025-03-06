import os

def list_contents(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    print("Directories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("\nFiles:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("\nAll Contents:")
    print(os.listdir(path))

path = input("Enter directory path: ")
list_contents(path)