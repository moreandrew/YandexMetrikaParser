import requests
import json

ym_token="yourtoken" # see the details about getting an access token in README 
ids="your counter id or ids"


def YMquery(startDate, endDate, searchEngine, startURL, token):
    adr="https://api-metrika.yandex.ru/stat/v1/data?ids="+ids+"&metrics=ym:s:visits,ym:s:bounceRate&startDate="\
        +startDate\
        +"&endDate="\
        +endDate\
        +"&accuracy=full&filters=(ym:s:startURL=~"\
        +startURL\
        +"AND%20ym:s:lastSearchEngineRoot=="\
        +searchEngine\
        +")&oauth_token="\
        +token

    r = requests.get(adr)
    parsed = json.loads(r.text)

    return parsed
    
    
    # Here's the page types I want to gather data for 
page_types = [
    ["All", "\'https://myexamplestore.com/\'"],
    ["Main Page", "\'https://myexamplestore.com/$\'"],
    ["All Mac Pages", "\'https://myexamplestore.com/brand/apple/macs/\'"],
    ["All Brands", "\'https://myexamplestore.com/brand/\'"],
    ["Just some page", "\'https://myexamplestore.com/sample_page/$\'"]
]


def main():
    # Set the parameters
    start_date = "2016-09-01"
    end_date = "2016-09-30"
    search_engine = "\'yandex\'" # or "\'google\'" for Google etc.
    
    # Let's write the results into a file
    f = open('output.txt', 'w')
    f.write("startDate: " + start_date + '\n'+"endDate: " + end_date+'\n'+'\n')
    f.write("-----Yandex-----"+'\n')
    i=0
    for counter in page_types:
        parsed = YMquery(start_date, end_date, search_engine, counter[1], ym_token)
        visits = parsed['data'][0]['metrics'][0]
        bounce_rate = parsed['data'][0]['metrics'][1]
        
        bounce_rate_formatted = round(bounce_rate, 2)/100
        result = counter[0] + '\t' + str(round(visits)) + '\t' + str(bounce_rate_formatted)
        
        f.write(result + '\n')
        i = i + 1
        print(str(i) + " of " + str(page_types.__len__()) + " parsed (Y)")

    f.close()


main()
