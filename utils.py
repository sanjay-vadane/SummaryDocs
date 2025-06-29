def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_summary(summary, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(summary)