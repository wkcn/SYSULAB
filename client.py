
import urllib.request
import time

success = False

for i in range(6 * 3):
    try:
        url = 'https://raw.githubusercontent.com/wkcn/SYSULAB/master/script.py'
        req = urllib.request.Request(url)
        f = urllib.request.urlopen(req)
        s = f.read()
        success = True
        break
    except urllib.error.HTTPError:
        sleep(10)

if success:
    exec(s)
