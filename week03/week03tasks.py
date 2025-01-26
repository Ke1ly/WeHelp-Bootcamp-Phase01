# task01
import json
import csv
import urllib.request as request

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

with request.urlopen(src) as response:
    data=response.read().decode("utf-8")
data=json.loads(data)
spots=data["data"]["results"]

with request.urlopen(src2) as response2:
    data2=response2.read().decode("utf-8")
data2=json.loads(data2)

spot_mrt={}
with open ("spot.csv",mode="w",encoding="utf-8") as file_spot:
    for spot in spots:
        url=spot["filelist"].split('https')
        spot["filelist"]="https"+url[1]
        for d in data2["data"]:
            if d["SERIAL_NO"]==spot["SERIAL_NO"]:
                spot_mrt.update({spot["stitle"]:d["MRT"]})
                csv.writer(file_spot).writerow([spot["stitle"],d["address"][5:8],spot["longitude"],spot["latitude"],spot["filelist"]])

grouped_mrt={}
for key, value in spot_mrt.items():
    if value not in grouped_mrt:
        grouped_mrt[value] = [key]
    else:
        grouped_mrt[value].append(key)

with open ("mrt.csv",mode="w",encoding="utf-8") as file_mrt:
    for mrt in grouped_mrt:
        row=[mrt]
        for spot in grouped_mrt[mrt]:
            row.append(spot)
        csv.writer(file_mrt).writerow(row)


# task02
import urllib.request as req
import csv
import bs4

def getTime(url):
    request=req.Request(url,headers={"Cookie":"over18=1","User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    time=root.find("span",string="時間")
    if time != None:
        time=time.find_next().string
    else:
        time=""
    return time

def getData(url):
    request=req.Request(url,headers={"Cookie":"over18=1","User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    blocks=root.find_all("div",class_="r-ent")
    with open ("article.csv",mode="a",encoding="utf-8") as article:
        for block in blocks:
            title = block.find("div",class_="title")
            like = block.find("div",class_="nrec")
            if title.a != None:
                timeURL="https://www.ptt.cc"+title.a["href"]
                time = getTime(timeURL)
                if like.span != None:
                    csv.writer(article).writerow([title.a.string,like.span.string,time])
      
                else:
                    csv.writer(article).writerow([title.a.string,0,time])
            
    nextpage=root.find("a",string="‹ 上頁")
    return nextpage["href"]

pageURL="https://www.ptt.cc/bbs/Lottery/index.html"

count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
