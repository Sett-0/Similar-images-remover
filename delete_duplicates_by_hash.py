# thanks to Alexander for quick code: https://stackoverflow.com/a/74751316
import hashlib
import os

hashes = set()

for filename in os.listdir("."):
    path = os.path.join(".", filename)
    digest = hashlib.sha1(open(path,'rb').read()).digest()
    if digest not in hashes:
        hashes.add(digest)
    else:
        os.remove(path)