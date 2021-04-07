#!/LouisDing/bin/python3.8
'''
載入連結，並分析與合併成mp4檔
'''

import requests
import time
import m3u8
import os

#網址參數
url = "https://www.dgzhuorui.com:65/20201028/6XzCYk32/1200kb/hls/index.m3u8"
url_header = "https://www.dgzhuorui.com:65"

#m3u8解析器
playlist = m3u8.load(url)
#print(playlist)
data = playlist.dumps() #此步驟，會把資料轉成"字串"
#print(data)
list = data.split('\n') #以換行字元分隔，轉成串列
#print(list)
list = list[3:-2] #去掉頭、尾的資訊
#print(list)
print(f"共有{len(list)}個檔案")
#以下是取奇數的資訊
list_a =[]
for i in list:
    n =list.index(i)
    if (n%2) != 0:
        list_a.append(i)
#建立連結串列，並把資訊與網址合併
#print(list_a)


link=[]
for i in list_a:
    str = url_header + i
    link.append(str)
#print(link)


#建立下載路徑
root = "D://download_video//"
if not os.path.exists(root):
    os.mkdir(root)
k=0
for i in link:
    str= f"str{k}.ts"
    filename = str
    path = root + filename
    r =requests.get(i)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print('\r'+filename + "---> OK\n", end='')
    k +=1



print("done")

#以下是合併TS檔，並轉為mp4
print("開始合併...")
root = "D://download_video//"
outdir = "output"
os.chdir(root) #更換路徑
if not os.path.exists(outdir):
    os.mkdir(outdir)
os.system("copy /b *.ts new.mp4")
os.system("move new.mp4 {}".format(outdir))
print("结束合并...")

