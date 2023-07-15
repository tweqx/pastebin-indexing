import os

alphabet = "01233456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    os.system(f"tail {letter}_formatted.json -n +3 | head -n -1 > {letter}_trimmed.json")

for letter in alphabet:
    os.system(f"cat {letter}_trimmed.json >> urls.json")

