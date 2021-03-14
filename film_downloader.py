#!/LouisDing/bin/python3.8
'''
建立影片連結的爬蟲
'''
import you_get
import urllib.request as req
from bs4 import BeautifulSoup

#此部分只建立爬蟲資訊，但是尚未出攜出m3u8的網址]

#建立網址
url="https://dramasq.cc/tw201025/"
request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"})
with req.urlopen(request) as response:
    content = response.read().decode("utf-8")
#print(data)
page_analysis = BeautifulSoup(content, "html.parser")
#print(page_analysis)
page_content = page_analysis.prettify()
#print(page_content)
sub_link = page_analysis.select("body > div.main.inner.sizing > div.content.sizing > div.episode.sizing > div.items.sizing > ul > li:nth-child(19) > a")[0].get('href')
#print(sub_link)
link = url+sub_link
#print(link)
subrequest = req.Request(link, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"})
with req.urlopen(subrequest) as response:
    content2 = response.read().decode("utf-8")
page_analysis2 = BeautifulSoup(content2, "html.parser").prettify()
#print(page_analysis2)

print(page_analysis2)
