
import requests
import csv
import time
import pickle
import json


token = '17954e0217954e0217954e025517e1e0ad1179517954e024808d7ef08a4aea213a676d9'
version = 5.124
count = 5000 # сколько постов?
offset = 100 # с какой поста? 
all_posts = []
T = True
s = 0
all_url = []


while T == True:
    domain = 'agressivniememes'

    
    response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'domain': domain,
                            'count': count, # сколько приходит постов
                            'offset': offset # первый пост

                        }
                        )
    data = response.json()['response']['items']
    all_posts.extend(data)
    offset += 1
    sumo = 5000 - offset
    print('Всего: ', offset, 'Осталось: ', sumo)


    for post in all_posts:
        try:
            if post['attachments'][0]['type']:
                url = post['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            pass
    
    all_url.append(url)
    if offset == 5000:
        T = False
        with open('all_url.txt', 'w') as f:
            f.write(json.dumps(all_url))
