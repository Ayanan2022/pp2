import shutil

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"File copied from {src} to {dest}.")
    except FileNotFoundError:
        print("Source file not found.")

src = input("Enter source file: ")
dest = input("Enter destination file: ")
copy_file(src, dest)