def create_text_file(filename):
    with open(filename, 'w') as f:
        for i in range(1, 10):
            line = str(i) * i  # Repeat the character i, i times
            print(line)

# Usage example
create_text_file('output.txt')