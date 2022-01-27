import requests
import re
import os

if __name__ == "__main__":
    #if not os.path.exists('./re'):
        #os.mkdir('./re')

    url = 'https://zh.moegirl.org.cn/zh-tw/%E9%AD%94%E5%A5%B3%E4%B9%8B%E6%97%85'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text

    ex = '<img.*?src="(.*?)".*?>'
    img_src_list = re.findall(ex, page_text, re.S)

    t=0
    with open('./re.html', 'w', encoding='utf-8') as fp:
        for src in img_src_list:
            fp.write(src+'\n')
            t+=1

    count = 0
    print('there are ',t, ' images'  )
    for src in img_src_list:
        img_data = requests.get(url=src,headers=headers).content
        img_name = src.split('/')[-1]
        img_path = './re/'+img_name
        with open(img_path, 'wb' ) as fp:
            fp.write(img_data)
            count +=1
            print(img_name,' success!!!', count, ' / ', t)
    print('finish!!')
