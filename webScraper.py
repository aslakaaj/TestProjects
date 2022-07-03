import urllib.request
from bs4 import BeautifulSoup

importedUrl = r"https://www.shopify.com/blog/motivational-quotes"
exportPath = r"C:\Users\Eier\OneDrive\Koding\PrøveProsjekt\quotes.txt"

urllib.request.urlretrieve(importedUrl, exportPath)

file = open("quotes.txt", "r", encoding="mbcs")
contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

f = open(r"quotes.txt", "w", encoding="utf-8")

for data in soup.find_all("li"):
    sum = data.get_text()
    f.writelines("\"" + sum + "\""+ ", \n")

f.close