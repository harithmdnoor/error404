import requests
import json
import time
from git import Repo
num = 0
while 1 == 1:
    print('server start time {}'.format(time.gmtime()))
    print('0% done')
    url1 = 'http://api.telegram.org/bot992148640:AAGqfJJyyvUkrMIZLI3fExfzzi6JiqriGdo/getupdates'
    x1 = requests.get(url1)
    rawJson1 = x1.json()
    url2 = 'http://api.telegram.org/bot992148640:AAGqfJJyyvUkrMIZLI3fExfzzi6JiqriGdo/getFile?file_id={}'.format(rawJson1['result'][-1]['message']['voice']['file_id'])
    x2 = requests.get(url2)
    rawJson2 = x2.json()
    print('30% done')
    url3 = 'http://api.telegram.org/file/bot992148640:AAGqfJJyyvUkrMIZLI3fExfzzi6JiqriGdo/{}'.format(rawJson2['result']['file_path'])
    x3 = requests.get(url3, allow_redirects=True)
    open('voice.mp3', 'wb').write(x3.content)
    time.sleep(10)
    print('50% done')
    repo_dir = 'C:/Users/harith/PycharmProjects/error404/.git'
    repo = Repo(repo_dir)
    file_list = [
        'C:\\Users\\harith\\PycharmProjects\\error404\\voice.mp3'
    ]
    commit_message = 'updated voice {}'.format(num)
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()
    print('100% done')
    print('code updated {} times'.format(num))
    num+=2

