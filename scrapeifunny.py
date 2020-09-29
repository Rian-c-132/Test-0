import requests
from bs4 import BeautifulSoup

url = "http://ifunny.co"

source = requests.get(url)
plain = source.text
soup = BeautifulSoup(plain, "html.parser")
urls = []
def get_urls():
	for link in soup.find_all("img"):
		#print("check")
		img_link = link.get('data-src')
		if img_link != None :
			urls.append(img_link)
	return urls
get_urls()
print(urls)