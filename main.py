import requests
import datetime
import random

oneday = datetime.timedelta(days=1)
oneday1=datetime.date.today()
yesterday = datetime.date.today() - oneday
x=yesterday.strftime('%Y%m%d')
y=oneday1.strftime('%Y%m%d')




url=("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/"+list1+"/daily/"+x+"12/"+y+"12")

headers = {
    'User-Agent': 'My User Agent 1.0',
}

response = requests.get(url, headers=headers)
data = response.json()
print(str(data['items'][0]['views']))

