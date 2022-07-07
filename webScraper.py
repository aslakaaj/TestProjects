import urllib.request
from bs4 import BeautifulSoup

importedUrl = input("Enter an URL to scrape \n")
exportPath = input("Enter an export file path: \n")
typeToScrape = input("What HTML element will you scrape for? \n")

urllib.request.urlretrieve(importedUrl, exportPath)

file = open("quotes.txt", "r", encoding="mbcs")
contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

f = open(r"quotes.txt", "w", encoding="utf-8")

for data in soup.find_all(typeToScrape):
    sum = data.get_text()
    f.writelines(sum + "\n")

f.close