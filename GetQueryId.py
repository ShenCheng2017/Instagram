import requests
import re

url='https://www.instagram.com/cheer_wr/'

baseURL='https://www.instagram.com'

def getQueryId(url,queryIds):
    response=requests.get(url)
    # response.encoding=response.apparent_encoding
    #print(response.status_code)

    jsSrc=re.findall(r'link rel=\"preload" href=\".*?\"',response.text)
    src=baseURL+jsSrc[0].split('\"')[3]
    #print(src)

    response=requests.get(src)
    #print(response.status_code)
    queryId=re.findall(r'queryId:\".*?\"',response.text)
    #print(queryId)

    for item in queryId:
        queryIds.append(item.split('\"')[1])




