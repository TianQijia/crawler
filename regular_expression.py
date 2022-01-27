import requests
import re
import os

URL = 'https://zh.moegirl.org.cn/zh-tw/%E9%AD%94%E5%A5%B3%E4%B9%8B%E6%97%85'
MAX_REATTEMPTS = 50
TIMEOUT = 3

if __name__ == "__main__":
    if not os.path.exists('./re'):
        os.mkdir('./re')

    page_text = requests.get(URL).text

    ex = '<img.*?src="(.*?)".*?>'
    img_src_list = re.findall(ex, page_text, re.S)
    total = len(img_src_list)

    with open('./re.html', 'w') as fp:
        for src in img_src_list:
            fp.write(src+'\n')

    count = 0
    print(f'There are {total} images')
    for src in img_src_list:
        print(src)
        img_name = src.split('/')[-1]
        img_path = './re/' + img_name
        for i in range(MAX_REATTEMPTS):
            try:
                img_data = requests.get(url=src, timeout=TIMEOUT).content
                with open(img_path, 'wb') as fp:
                    fp.write(img_data)
                count += 1
                print(f"{img_name} succeed!!! {count}/{total}")
                break

            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
                pass

            except requests.exceptions.MissingSchema:
                break

    print('finished!!')
