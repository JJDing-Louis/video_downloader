#!/LouisDing/bin/python3.8

import requests
import m3u8
import urllib.request as req
from bs4 import BeautifulSoup
import os

url = input("請輸入m3U8網址: ")
url_page = input("輸入影片網址: ")
download_path = input("請輸入下載路徑: ")
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

def get_m3u8(m3u8_url):
    playlist = m3u8.load(m3u8_url)
    data = playlist.dumps()
    list = data.split('\n')  # 以換行字元分隔，轉成串列
    list = list[3:2059]  # 去掉頭、尾的資訊
    list_content = []
    for i in list:
        if (list.index(i)%2) != 0:
            list_content.append(i)
    return list_content

def get_url_header(url):
    first = url.find("index")
    url_header = url[:first]
    return url_header

def analysis_download_link(url_header, list_content):
    link=[]
    for i in list_content:
        str = url_header+ i
        link.append(str)
    return link

def download_ts(link,download_path, list_content):
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    for i in link:
        for j in list_content:
            '''filename = i[-20:]'''
            path = download_path + j
            r = requests.get(i)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('\r' + j + "---> OK", end='')
    return True

def get_filename(link):
    request = req.Request(link, headers=header)
    with req.urlopen(request) as response:
        content = response.read().decode("utf-8")
    page_analysis = BeautifulSoup(content, "html.parser")
    page_title = page_analysis.select("#htitle")[0].text
    return page_title

def m3u8_to_mp4(link):
    print("開始合併!")
    outdir ="output"
    file_name = get_filename(link)
    os.chdir(download_path)  # 更換路徑
    if not os.path.exists(outdir):
        os.mkdir(outdir) #建立路徑
    #以下是合併檔案(需再研究)
    os.system("copy /b *.ts"+".mp4")
    os.system("move new.mp4 {}".format(outdir))
    print("结束合并...")


a = get_m3u8(url)
b =get_url_header(url)
c = analysis_download_link(b,a)
print(a)
print(b)
print(c)



