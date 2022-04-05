import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(blockchain_dir + filename, mode='rb').read()

    return hashlib.md5(file).hexdigest()


def create_genesis():
    if not os.path.isdir(blockchain_dir):
        os.mkdir(blockchain_dir)

        with open(blockchain_dir + '1', mode='w') as file:
            file.write("Genesis block\n")
