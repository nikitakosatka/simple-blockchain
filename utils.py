import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(blockchain_dir + filename, mode='rb').read()

    return hashlib.md5(file).hexdigest()
