url1 = "https://api.pushshift.io/reddit/search/comment/?subreddit=finance&size=1000"

base = datetime.datetime.today()
dateList = [base - datetime.timedelta(days=x) for x in range(0, 4524)]
dateList = [str(x)[:10] for x in dateList]
secondDateList = dateList[1:]


redditComments = {}
for i in range(0, len(secondDateList)):
    print('going')
    before = dateList[i]
    after = secondDateList[i]
    url = "https://api.pushshift.io/reddit/search/comment/?subreddit=finance&size=1000&before=" + before + '&after=' + after
    r = requests.get(url)
    data = r.json()
    redditComments[before] = data['data']
    
import json

with open('data.json', 'w') as fp:
    json.dump(redditComments, fp)
    
