from bs4 import BeautifulSoup
import requests

#Scrap the given website
url = 'https://scrapingclub.com/exercise/list_basic/'
count = 1
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#Find the items
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

#Scrape a single page of data
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1

#Scrape multiple pages of data
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('a', class_='page-link')
urls = []

for page in pages:
    #Remove next or previous words
    pageNum = int(page.text) if page.text.isdigit() else None
    if pageNum != None:
        #Get the next page link
        link = page.get('href')
        urls.append(link)

#Loop over the pages
for i in urls:
    response = requests.get(url + i)
    soup = BeautifulSoup(response.text, 'lxml')

    #Get the items
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    
    #Loop over the items
    #Print the count, item price, and item name
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1

#Run py scrapePages.py in the terminal (Windows)