"""
Scans all files in the current directory, calculates their hashes, and lists duplicate images based on identical content.
"""

import os
import hashlib

hashes = {}
duplicates = []

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash in hashes:
            duplicates.append(filename)
        else:
            hashes[filehash] = filename

for duplicate in sorted(duplicates):
    print(duplicate)