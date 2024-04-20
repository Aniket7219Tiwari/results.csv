import requests
from bs4 import BeautifulSoup
data=[]
obj={}
target_website = "https://www.yellowpages.com/new-york-ny/restaurants"
resp = requests.get(target_website)
soup=BeautifulSoup(resp.text, 'html.parser')
allResults = soup.find_all("div",{"class":"result"})
for i in range(0,len(allResults)):
    try:
        lateral_string=allResults[i].find("a",{"class":"business-name"}).get('href')
    except:
        lateral_string=None
    target_website = 'https://www.yellowpages.com{}'.format(lateral_string)
    print(lateral_string)
    resp = requests.get(target_website).text
    soup=BeautifulSoup(resp, 'html.parser')
    try:
        obj["Website"]=soup.find("p",{"class":"website"}).find("a").get("href")
    except:
        obj["Website"]=None
    try:
        obj["Email"]=soup.find("a",{"class":"email-business"}).get('href').replace("mailto:","")
    except:
        obj["Email"]=None
    data.append(obj)
    obj={}
print(data)
