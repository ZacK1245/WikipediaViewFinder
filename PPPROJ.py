import requests
import datetime
import time

oneday = datetime.timedelta(days=1)
oneday1=datetime.date.today()
yesterday = datetime.date.today() - oneday
x=yesterday.strftime('%Y%m%d')
y=oneday1.strftime('%Y%m%d')

# first get all lines from file
with open('company.txt', 'r') as w:
    companies = w.readlines()

# remove spaces
companies = [line.replace(' ', '') for line in companies]

# finally, write lines in the file
with open('company.txt', 'w') as w:
    w.writelines(companies)

f = open("company.txt","r")
lines = f.readlines()
r=f.read()
for line in lines:
    print(str(line)+"l")
    url=("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/"+str(line)+"/daily/"+str(x)+"12/"+str(y))

    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    print(url)
    response = requests.get(url, headers=headers)
    data = response.json()
    print(str(data['items'][0]['views'])+" -> "+line)

    

