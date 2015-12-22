import hashlib
import sys
import os
import os.path

hashes = {}


def md5(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()


def add_hash(hash, fname):
    matches = hashes.setdefault(hash, [])
    if matches:
        print("Possible match|{0}|{1}|{2}".format(hash, fname, matches[0]))
    matches.append(fname)


def hash_paths(paths):
    for path in paths:
        for root, _, files in os.walk(path):
            for f in files:
                fname = os.path.join(root, f)
                add_hash(md5(fname), fname)


if __name__ == '__main__':
    hash_paths(sys.argv[1:])
