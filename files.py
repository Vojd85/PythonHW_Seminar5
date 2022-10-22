def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def add_file(path, val):
    with open(path, 'a') as file:
        file.write(f'{val}\n')