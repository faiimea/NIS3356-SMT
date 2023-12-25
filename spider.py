from requests import get

url = "https://www.zhihu.com/api/v3/feed/topstory/recommend"
list = []

while (len(list) < 20):
    a = get(url).json()['data']
    for i in range(len(a)):
        # print(a[i]['target']['question']['title'])
        tmp = a[i]['target']
        try:
            list.append(tmp['question']['title'])
        except:
            continue
            
for i in list:
    print(i)