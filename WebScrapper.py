import requests #Install libs, requests, beautifulsoup4 and inflection
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = [] #create an empty list
    
    def post_formatter(url):
        if 'post' in url: #we are only want to link has a post inside
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

    for link in links:
        if  link.get('href') == None:
            continue
        else:
           post_formatter(link.get('href'))

    return titles

r = requests.get('https://www.dailysmarty.com/topics/python') #here the web page link
soup = BeautifulSoup(r.text, 'html.parser') #here parser what you looking for
links = soup.find_all('a') #web links have an a tag

titles = title_generator(links)
for title in titles:
    print(title)
