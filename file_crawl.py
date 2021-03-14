#!/LouisDing/bin/python3.8
'''

'''
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://dramasq.cc/tw201025/1.html"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
request = req.Request(url, headers=header)
with req.urlopen(request) as response:
    content = response.read().decode("utf-8")
page_analysis = BeautifulSoup(content, "html.parser")
page_content = page_analysis.prettify()
txt = page_analysis.select("#htitle")[0].text
print(txt)