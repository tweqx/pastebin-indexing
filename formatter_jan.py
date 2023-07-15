import os

alphabet = "01233456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    os.system(f"jq '. | flatten(1) | map(\"https://web.archive.org/web/\" + .[1] + \"/\" + .[2])' -s {letter}.json > {letter}_formatted.json")
