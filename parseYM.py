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
pageTypes = [
    ["All", "\'https://myexamplestore.com/\'"],
    ["Main Page", "\'https://myexamplestore.com/$\'"],
    ["All Mac Pages", "\'https://myexamplestore.com/brand/apple/macs/\'"],
    ["All Brands", "\'https://myexamplestore.com/brand/\'"],
    ["Just some page", "\'https://myexamplestore.com/sample_page/$\'"]
]

def main():

    # Set the parameters
    startDate = "2016-09-01"
    endDate = "2016-09-30"
    searchEngine = "\'yandex\'" # or "\'google\'" for Google etc.
    # Let's write the results into a file
    f = open('output.txt', 'w')
    f.write("startDate: "+startDate+'\n'+"endDate: "+endDate+'\n'+'\n')
    f.write("-----Yandex-----"+'\n')
    i=0
    for counter in pageTypes:
        parsed = YMquery(startDate, endDate, searchEngine, counter[1], ym_token)
        visits = parsed['data'][0]['metrics'][0]
        bounceRate = parsed['data'][0]['metrics'][1]
        brFormatted = round(bounceRate, 2)/100
        result = counter[0]+'\t'+str(round(visits))+'\t'+str(brFormatted)
        f.write(result+'\n')
        i=i+1
        print(str(i)+" of "+str(pageTypes.__len__())+" parsed (Y)")

    f.close()


main()