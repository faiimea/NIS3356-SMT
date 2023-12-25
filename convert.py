import json
import csv
from requests import get
from tqdm import tqdm
from time import sleep
import os

file = open('res.csv', 'a', newline='')
writer = csv.writer(file)
url = "https://api.zhihu.com/questions/"

num = 1
for _, _, files in os.walk('./data'):
    total_num = len(files)
    for file in files:
        print('{}/{}'.format(num, total_num))
        with open('./data/' + file, "r", encoding="UTF-8") as file:
            data = json.load(file)
            
        for i, v in tqdm(data.items()):
            id = int(i)
            a = get(url + i)
            if a.status_code == 403:
                print('\033[0;31;40m被ban了！\033[0m')
                exit(0)
            elif a.status_code == 404:
                continue
            time = a.json()['created']
            writer.writerows([[str(time), v['title']]])
        num += 1
        sleep(0.2)