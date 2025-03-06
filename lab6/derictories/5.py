def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print("List written to file successfully.")

data = ["Apple", "Banana", "Cherry"]
file_path = "output.txt"
write_list_to_file(file_path, data)