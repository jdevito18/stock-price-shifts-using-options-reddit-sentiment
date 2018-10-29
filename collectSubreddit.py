## mining with subreddit titles
import datetime
import requests
import time
import json 
base = datetime.datetime.today()
dateList = [base - datetime.timedelta(days=x) for x in range(0, 4524)]
dateList = [str(x)[:10] for x in dateList]
secondDateList = dateList[1:]


redditPosts = {}
for i in range(0, len(secondDateList)):
    if i % 100 == True:
        print(str(i-1) + 'days have been downloaded so far')
        with open('titleData.json', 'w') as fp:
            json.dump(redditPosts, fp)
    before = dateList[i]
    after = secondDateList[i]
    url = "https://api.pushshift.io/reddit/search?subreddit=finance&size=1000&before=" + before + '&after=' + after + '&filter=title'
    try:
        r = requests.get(url)
    except:
        print('fuck its not working')
        time.sleep(5)
    data = r.json()
    redditPosts[before] = data['data']

with open('titleData.json', 'w') as fp:
    json.dump(redditPosts, fp)
