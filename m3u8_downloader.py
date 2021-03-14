#!/LouisDing/bin/python3.8
'''
載入連結，並分析與合併成mp4檔
'''


import requests
import m3u8
import os

#網址參數
url = "https://youku.cdn31-okzy.com/20201102/458_4aacade3/1000k/hls/index.m3u8"
url_header = "https://youku.cdn31-okzy.com/20201102/458_4aacade3/1000k/hls/"

#m3u8解析器
playlist = m3u8.load(url)

data = playlist.dumps() #此步驟，會把資料轉成"字串"
list = data.split('\n') #以換行字元分隔，轉成串列
list = list[3:2059] #去掉頭、尾的資訊
#以下是取奇數的資訊
list_a =[]
for i in list:
    n =list.index(i)
    if (n%2) != 0:
        list_a.append(i)
#建立連結串列，並把資訊與網址合併
link=[]
for i in list_a:
    str = url_header + i
    link.append(str)

#建立下載路徑
root = "D://download_video//"
if not os.path.exists(root):
    os.mkdir(root)
for i in link:
    filename = i[-20:]
    path = root + filename
    r =requests.get(i)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print('\r'+filename + "---> OK", end='')
print("done")

#以下是合併TS檔，並轉為mp4
print("開始合併...")
root = "D://download_video//"
outdir = "output"
os.chdir(root)
if not os.path.exists(outdir):
    os.mkdir(outdir)
os.system("copy /b *.ts new.mp4")
os.system("move new.mp4 {}".format(outdir))
print("结束合并...")

