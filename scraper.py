import json
import requests
from bs4 import BeautifulSoup

keyword = 'mouse'
# page_number = 8
headers = {
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'
}
results = []
for i in range(1, 11):
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + \
        keyword+'&_pgn='+str(i)
    # r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw='+keyword, headers = headers)
    r = requests.get(url, headers=headers)
    print('r.status_code=', r.status_code)
    #print('url=', url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # seperately extract names and prices
    '''
    names = soup.select('.s-item__title')
    for name in names:
        print ('name=',name.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=', price.text)
    '''
    # extract the 'item boxes'

    #boxes = soup.select('li.s-item--watch-at-corner.s-item')
    boxes = soup.select('.clearfix.s-item__wrapper')
    for box in boxes:
        # print('---')
        result = {}
        names = box.select('.s-item__title')
        for name in names:
            #print ('name=',name.text)
            result['name'] = name.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price=', price.text)
            result['price'] = price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
            #print('status=', status.text)
            result['status'] = status.text
        #print('result=', result)
        results.append(result)

    print('len(results)=', len(results))

j = json.dumps(results)
with open('items.json', 'w') as f:
    f.write(j)
# print('j=', j)
