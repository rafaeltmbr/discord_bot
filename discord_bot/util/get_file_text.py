def get_file_text(file_path: str):
    with open(file_path) as file:
        return file.read()
