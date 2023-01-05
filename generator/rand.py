import os
import json
from random import randint

from lib import create_dir, write_file



def main() :

    if os.path.exists('docs/api/joke') :
        with open('docs/api/jokes/index.json', 'r', encoding='utf-8') as f :
            data = json.load(f)
            create_dir('docs/api/joke/random')
            write_file('docs/api/joke/random/index.json', json.dumps(data[randint(0,len(data)-1)], ensure_ascii=False, indent=4))
        if os.path.exists('docs/api/jokes/lang'):
            for lang in os.listdir('docs/api/jokes/lang'):
                with open(f'docs/api/jokes/lang/{lang}/index.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    create_dir(f'docs/api/joke/random/{lang}')
                    write_file(f'docs/api/joke/random/{lang}/index.json', json.dumps(data[randint(0,len(data)-1)], ensure_ascii=False, indent=4))
            


if __name__ == '__main__' :
    main()
    os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
    os.system('git config --local user.name "github-actions[bot]"')
    os.system('git add .')
    os.system('git commit -m "api update random"')
    os.system('git push')   