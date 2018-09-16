import requests
import bs4

res = requests.get('http://doko.dwit.edu.np/class/show/6')

soup = bs4.BeautifulSoup(res.text,"lxml")
main = soup.find_all('div',{"class":"container"})
#match = soup.find_all('div',{ "class":"modal-header"})
#content=soup.find_all('div',{ "class":"modal-content"})
record= []
for item in main:
    f = item.find_all("div",{"class":"modal-header"})
    for a in f:
        d={}
        d["name"]= a.find_all("span",{"class":"text-capitalize"})[0].text
        record.append((d))
#print(record)
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)




writeToJSONFile('./','data_name',record)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name
