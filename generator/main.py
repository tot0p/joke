import json
import os

def main():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in range(len(data)):
            data[item]['id'] = item
    create_dir('api')
    create_By_Id(data)
    create_All(data)
    create_By_lang(data)
    create_By_author(data)


def create_All(data: list):
    create_dir('api/items')
    write_file('api/items/index.json', json.dumps(data, ensure_ascii=False, indent=4))

def create_By_Id(data: list):
    for item in data:
        create_dir('api/id')
        create_dir(f'api/id/{item["id"]}')
        write_file(f'api/id/{item["id"]}/index.json', json.dumps(item, ensure_ascii=False, indent=4))

def create_By_lang(data: list):
    for item in data:
        create_dir('api/lang')
        create_dir(f'api/lang/{item["lang"]}')
        write_file(f'api/lang/{item["lang"]}/index.json', json.dumps(item, ensure_ascii=False, indent=4))

def create_By_author(data: list):
    for item in data:
        create_dir('api/author')
        create_dir(f'api/author/{item["author"]}')
        write_file(f'api/author/{item["author"]}/index.json', json.dumps(item, ensure_ascii=False, indent=4))


def create_dir(dir_name: str):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def write_file(file_name: str, data: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)

if __name__ == '__main__':
    main()
    
    os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
    os.system('git config --local user.name "github-actions[bot]"')
    os.system('git add api')
    os.system('git add api/*')
    os.system('git commit -m "api update"')
    os.system('git push origin/api')    

