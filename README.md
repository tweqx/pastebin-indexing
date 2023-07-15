This repository is a collection of scripts I used to get all archived pastes on the Wayback Machine.

### Querying the list of all pastebin.com links archived
```bash
python3 indexer.py
python3 formatter.py
python3 collector.py
cat urls.json | awk '{ print substr($1, 2, length($1)-3) }' | grep pastebin.com | uniq > urls_list.txt
```

Then, everything but `urls_list.txt` can be deleted: `rm *.json`

### Querying everything that has been archived in january
```bash
python3 indexer_jan.py
python3 formatter_jan.py
cat urls.json | awk '{ print substr($1, 2, length($1)-3) }' | grep pastebin.com > archived_in_january.txt
```

Then, everything but `archived_in_january.txt` can be deleted: `rm *.json`

