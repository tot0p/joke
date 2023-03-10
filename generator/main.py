import json
import os
from lib import create_dir, write_file

import rand

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
    create_by_lang_category(data)
    

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
        t = item['category'].split(',')
        for i in t:
            if i not in temp.keys():
                temp[i] = [item]
            else:
                temp[i].append(item)
    for key in temp.keys():
        create_dir('docs/api/jokes/category')
        create_dir(f'docs/api/jokes/category/{key}')
        write_file(f'docs/api/jokes/category/{key}/index.json', json.dumps(temp[key], ensure_ascii=False, indent=4))


def create_by_lang_category(data: list):
    temp = {}
    for item in data:
        if item['lang'] not in temp.keys():
            temp[item['lang']] = {}
        t = item['category'].split(',')
        for i in t:
            if i not in temp[item['lang']].keys():
                temp[item['lang']][i] = [item]
            else:
                temp[item['lang']][i].append(item)
    for key in temp.keys():
        create_dir(f'docs/api/jokes/lang/{key}/category')
        for key2 in temp[key].keys():
            create_dir(f'docs/api/jokes/lang/{key}/category/{key2}')
            write_file(f'docs/api/jokes/lang/{key}/category/{key2}/index.json', json.dumps(temp[key][key2], ensure_ascii=False, indent=4))

if __name__ == '__main__':
    main()
    

    rand.main()
    os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
    os.system('git config --local user.name "github-actions[bot]"')
    os.system('git add .')
    os.system('git commit -m "api update"')
    os.system('git push')    

