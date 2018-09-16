import requests
import bs4

res = requests.get('http://doko.dwit.edu.np/class/show/6')

soup = bs4.BeautifulSoup(res.text,"lxml")
main = soup.find_all('div',{"class":"container"})
#match = soup.find_all('div',{ "class":"modal-header"})
#content=soup.find_all('div',{ "class":"modal-content"})
record= []
for item in main:
    f = item.find_all("div",{"class":"modal-content"})
    for a in f:

        content= a.text
        record.append((content))
import pandas as pd
df=pd.DataFrame(record, columns=['content'])
print(df.to_csv("data2.csv", index=False, encoding='utf-8'))
