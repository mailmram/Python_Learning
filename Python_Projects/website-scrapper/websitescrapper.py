import requests
from bs4 import BeautifulSoup
import pandas as p

r = requests.get("https://www.century21.com/real-estate/kirkland-wa/LCWAKIRKLAND/")
c = r.content
s = BeautifulSoup(c, "html.parser")
all = s.find_all("div", {"class":"property-card-primary-info"})
#print(all[0].text)
# all = s.find_all("a", {"class":"listing-price"})
# allAddress = s.find_all("div", {"class":"property-address-info"})
# allRoomsBath = s.find_all("div", {"class":"col-wrap-mid"})
#print(allRoomsBath[0].text.replace("\n","").replace("  ",""))
#print(allAddress[0].text.replace("\n","").replace("  ",""))
l = []
for item in all:
    d = {}

    d["price"] = item.find("a", {"class":"listing-price"}).text.replace(" ", "").replace("\n","")
    d["address"] = item.find("div", {"class":"property-address-info"}).text.replace("\n","").replace("  ","")
    d["rooms"] = item.find("div", {"class":"col-wrap-mid"}).text.replace("\n","").replace("  ","")
    l.append(d)
df = p.DataFrame(l)
print(df)
df.to_csv("Output.csv")
    #item = item.text.replace(" ", "").replace("\n","")
    #print(item)
#print (all[0].text.replace(" ","").replace("\n",""))
