import requests
import re
from bs4 import BeautifulSoup
import csv

import time
import DownImgs

headersURL={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}



def instagram(Data,nickname,ptr):
    for item in range(ptr,len(Data['shortcode'])):
        url = 'https://www.instagram.com/p/'+Data['shortcode'][item]+'/?taken-by='+nickname

        response=requests.get(url)
        print(url,response.status_code)

        post_time = time.strftime('%Y-%m-%d %H.%M.%S ', time.localtime(Data['post_time'][item]))
        get_time=time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(Data['post_time'][item]))
        soup=BeautifulSoup(response.content,'lxml')
        titles=soup.select('head > title')
        title=titles[0].get_text()
        data={
            'get-time':get_time,
            'title':title
        }
        with open(nickname+'/ins_contents_log.csv','a',encoding='utf-8-sig',newline='') as f:
            fieldnames=['get-time','title']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow(data)


        img_url=re.findall(r'\"display_url\":\".*?jpg',response.text)
        if len(img_url)==1:
            img_url[0] = 'https:' + img_url[0].split(':')[2]
            # print(img_url[i])
            DownImgs.downImgs(post_time, 0, img_url[0],nickname)
            print('done')
            time.sleep(2)
        else:
            for i in range(1,len(img_url)):
                img_url[i]='https:'+img_url[i].split(':')[2]
                #print(img_url[i])
                DownImgs.downImgs(post_time,i, img_url[i],nickname)
                print('done')
                time.sleep(2)
        video_url=re.findall(r'\"video_url\":\".*?mp4',response.text)
        if len(video_url)>=1:
            for i in range(len(video_url)):
                video_url[i]=video_url[i].split('\"')[3]
                #print(img_url[i])
                DownImgs.downVideos(post_time,i, video_url[i],nickname)
                print('done')
                time.sleep(2)
        time.sleep(1)



