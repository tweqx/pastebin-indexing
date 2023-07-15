import json
import requests
import time
import re
import datetime

with open('./archived_in_january.txt', 'r') as f:
    o = f.read().split()

entries = {}

try:
    i = 0
    while i < len(o):
        url = o[i]

        try:
            # timestamp, url
            l = [
                0,
                url[len("https://web.archive.org/web/"):len("https://web.archive.org/web/20120111070738")],
                url[len("https://web.archive.org/web/20120111070738/"):]
            ]
            url = f"http://web.archive.org/web/{l[1]}id_/{l[2]}"
            timestamp = datetime.datetime.strptime(l[1], "%Y%m%d%H%M%S")

            if l[2].startswith('https://pastebin.com/share.php') or l[2].startswith('http://pastebin.com/share.php') or l[2].startswith('http://pastebin.com:80/share.php') or l[2].startswith('https://pastebin.com:80/share.php'):
                i += 1
                continue
            r = requests.get(url)
            
            print(l[2])
            
            try:
                n = r.text.index('<ul class="right_menu"><li>')
                public_pastes = r.text[n:r.text.index('\n', n)]
                for name, sec in re.findall('<li><a href="/(........)">.*?</a><span>(\d*) sec ago</span></li>', public_pastes):
                    time = timestamp - datetime.timedelta(seconds=int(sec))
                    
                    if not name in entries:
                        entries[name] = time
            except:
                print(url)

            i += 1
        except Exception as e:
            print(e)
except:
    s = repr(entries)
    f = open('timestamps', 'w')
    f.write(s)
    f.close()

    print(entries)
