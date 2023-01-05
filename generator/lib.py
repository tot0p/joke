import os
import json

def create_dir(dir_name: str):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def write_file(file_name: str, data: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)
