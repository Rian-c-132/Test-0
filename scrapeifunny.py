import requests
from bs4 import BeautifulSoup


urls = []
def get_urls(site):
	if site == 'ifunny' :
		url = "https://www.ifunny.co/"
	else :
		url = "https://www.memedroid.com/"

	source = requests.get(url)
	soup = BeautifulSoup(source.text, "lxml")

	if site == 'ifunny' :
		for link in soup.find_all("img"):
			img_link = link.get('data-src')
			if img_link != None :
				urls.append(img_link)
	else :
		for link in soup.find_all("img", {'class': 'img-responsive'}):
			img_link = link.get('src')
			if img_link[:4] == 'http' :
				urls.append(img_link)
	return urls
#get_urls()
#print(urls)