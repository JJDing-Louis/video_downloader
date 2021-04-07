#!/LouisDing/bin/python3.8
'''
載入連結，並分析與合併成mp4檔
'''

import requests
import m3u8
import os
import time

#網址參數
url = "https://cdn003.wokuzy.com/s03/d/0/0/ae3f99dd9f6c46c8d6b95a7658f89/hls/h264/index.m3u8"
url_header = "https://cdn003.wokuzy.com/s03/d/0/0/ae3f99dd9f6c46c8d6b95a7658f89/hls/h264/"

#m3u8解析器
playlist = m3u8.load(url)
#print(playlist)
data = playlist.dumps() #此步驟，會把資料轉成"字串"
#print(data)
list = data.split('\n') #以換行字元分隔，轉成串列
#print(list)
list = list[4:-2] #去掉頭、尾的資訊
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
subroot = root+"download_buffer//"
if not os.path.exists(subroot):
    os.mkdir(subroot)
    #os.chdir()


for i in link:
    filename = i[-6:]
    path = subroot + filename
    r =requests.get(i)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print('\r'+filename + "---> OK", end='')
        time.sleep(2)
        #WYun
print("done")

#以下是合併TS檔，並轉為mp4
print("開始合併...")
#root = "D://download_video//"
outdir = "output"
os.chdir(root) #更換路徑
if not os.path.exists(outdir):
    os.mkdir(outdir)
os.system("copy /b *.ts new.mp4")
os.system("move new.mp4 {}".format(outdir))

print("结束合并...")

