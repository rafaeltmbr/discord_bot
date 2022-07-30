def get_file_lines(file_path: str):
    lines: list[str] = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()

            if line:
                lines.append(line)

    return lines
