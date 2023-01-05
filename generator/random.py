import os
import json
import random

from lib import create_dir, write_file



def main() :

    if os.path.exists('docs/api/joke') :
        with open('data.json', 'r', encoding='utf-8') as f :
            data = json.load(f)
            random.shuffle(data)
            create_dir('docs/api/joke/random')
            write_file('docs/api/joke/random/index.json', json.dumps(data[0], ensure_ascii=False, indent=4))
        if os.path.exists('docs/api/jokes/lang'):
            for lang in os.listdir('docs/api/jokes/lang'):
                with open(f'docs/api/jokes/lang/{lang}/index.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    random.shuffle(data)
                    create_dir(f'docs/api/joke/random/{lang}')
                    write_file(f'docs/api/joke/random/{lang}/index.json', json.dumps(data[0], ensure_ascii=False, indent=4))
            


if __name__ == '__main__' :
    main()