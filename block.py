import json

from utils import *


def check_integrity():
    files = sorted(os.listdir(blockchain_dir), key=lambda x: int(x))

    results = []

    for file in files[1:]:
        h = json.load(open(blockchain_dir + file))['hash']
        prev_file = str(int(file) - 1)

        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'

        else:
            res = 'Bad'

        results.append({'block': prev_file, 'result': res})

    return results


def write_block(sender, amount, recipient):
    files = sorted(os.listdir(blockchain_dir), key=lambda x: int(x))
    last_file = files[-1]
    filename = str(int(last_file) + 1)

    prev_hash = get_hash(last_file)

    data = {
        'sender': sender,
        'amount': amount,
        'recipient': recipient,
        'hash': prev_hash
    }

    with open(blockchain_dir + filename, mode='w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
