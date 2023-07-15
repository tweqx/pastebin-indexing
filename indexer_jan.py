import os

alphabet = "01233456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    os.system(f"wget 'http://web.archive.org/cdx/search/cdx?url=pastebin.com/{letter}*&output=json&from=201201&to=201201' -O {letter}.json -v")
