import json
import os

def main():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in range(len(data)):
            data[item]['id'] = item
    rm_dirRecursive('docs/api')
    create_dir('docs/api')
    create_dir('docs/api/joke')
    create_By_Id(data)
    create_All(data)
    create_By_lang(data)
    create_By_author(data)
    create_By_category(data)

def rm_dirRecursive(dir_name: str):
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(dir_name)


def create_All(data: list):
    create_dir('docs/api/jokes')
    write_file('docs/api/jokes/index.json', json.dumps(data, ensure_ascii=False, indent=4))

def create_By_Id(data: list):
    for item in data:
        create_dir('docs/api/joke/id')
        create_dir(f'docs/api/joke/id/{item["id"]}')
        write_file(f'docs/api/joke/id/{item["id"]}/index.json', json.dumps(item, ensure_ascii=False, indent=4))

def create_By_lang(data: list):
    temp = {}
    for item in data:
        if item['lang'] not in temp.keys():
            temp[item['lang']] = [item]
        else:
            temp[item['lang']].append(item)
    for key in temp.keys():
        create_dir('docs/api/jokes/lang')
        create_dir(f'docs/api/jokes/lang/{key}')
        write_file(f'docs/api/jokes/lang/{key}/index.json', json.dumps(temp[key], ensure_ascii=False, indent=4))

def create_By_author(data: list):
    temp = {}
    for item in data:
        if item['author'] not in temp.keys():
            temp[item['author']] = [item]
        else:
            temp[item['author']].append(item)
    for key in temp.keys():
        create_dir('docs/api/jokes/author')
        create_dir(f'docs/api/jokes/author/{key}')
        write_file(f'docs/api/jokes/author/{key}/index.json', json.dumps(temp[key], ensure_ascii=False, indent=4))


def create_By_category(data: list):
    temp = {}
    for item in data:
        if item['category'] not in temp.keys():
            temp[item['category']] = [item]
        else:
            temp[item['category']].append(item)
    for key in temp.keys():
        create_dir('docs/api/jokes/category')
        create_dir(f'docs/api/jokes/category/{key}')
        write_file(f'docs/api/jokes/category/{key}/index.json', json.dumps(temp[key], ensure_ascii=False, indent=4))

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
    os.system('git add .')
    os.system('git commit -m "api update"')
    os.system('git push')    

