import json
import os

def main():
    with open('../data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in range(len(data)):
            data[item]['id'] = item
    create_dir('../api')
    write_file('../api/all.json', json.dumps(data, ensure_ascii=False, indent=4))
    create_By_Id(data)


def create_By_Id(data: list):
    for item in data:
        create_dir(f'../api/{item["id"]}')
        write_file(f'../api/{item["id"]}/index.json', json.dumps(item, ensure_ascii=False, indent=4))


def create_dir(dir_name: str):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def write_file(file_name: str, data: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)

if __name__ == '__main__':
    main()
    

