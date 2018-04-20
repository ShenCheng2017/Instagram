import requests
import os

# url='https://scontent-lga3-1.cdninstagram.com/vp/44e51d7b8189513351db8c9550318a5a/5B70DB7C/t51.2885-15/e35/29738212_219613082123859_7065281357231947776_n.jpg'

headers={
    'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'referer': 'https://www.instagram.com/p/BheWRXIg-8x/?taken-by=cheer_wr',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}



def downImgs(item,i,url,nickname):
    response = requests.get(url, headers=headers)
    print(url,response.status_code)

    open(nickname+'/Images/'+item+str(i)+'.jpg','wb').write(response.content)
def downVideos(item,i,url,nickname):
    response = requests.get(url)
    print(url,response.status_code)

    open(nickname+'/Images/'+item+str(i)+'.mp4','wb').write(response.content)

