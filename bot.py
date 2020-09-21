import requests
import json
from git import Repo
url1 = 'http://api.telegram.org/bot992148640:AAGqfJJyyvUkrMIZLI3fExfzzi6JiqriGdo/getupdates'
x1 = requests.get(url1)
rawJson1 = x1.json()
url2 = 'http://api.telegram.org/bot992148640:AAGqfJJyyvUkrMIZLI3fExfzzi6JiqriGdo/getFile?file_id={}'.format(rawJson1['result'][-1]['message']['voice']['file_id'])
x2 = requests.get(url2)
rawJson2 = x2.json()
url3 = 'http://api.telegram.org/file/bot992148640:AAGqfJJyyvUkrMIZLI3fExfzzi6JiqriGdo/{}'.format(rawJson2['result']['file_path'])
x3 = requests.get(url3, allow_redirects=True)
open('voice.mp3', 'wb').write(x3.content)

repo_dir = 'error404'
repo = Repo(repo_dir)
file_list = [
    'C:/Users/harith/PycharmProjects/error404Bot/voice.mp3'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()