# INTRO TO WEB SCRAPPING WITH BEAUTIFUL SOUP

import requests
from bs4 import BeautifulSoup
import json
from csv import writer

response = requests.get('https://dubai.dubizzle.com/en/property-for-sale/residential/villahouse/?filters=(bedrooms%3E%3D3%20AND%20bedrooms%3C%3D3)%20AND%20(amenities_v2.value%3A%22maids_room%22)')

soup = BeautifulSoup(response.text,'html.parser')

posts = soup.find_all(class_='ListItem__Root-sc-1i3osc0-1 hMPXKC')

with open('posts.csv', 'w') as file:
    csv_writer = writer(file)
    headers = ['name', 'price', 'floorsize']
    csv_writer.writerow(headers)

    for post in posts:
        data = json.loads(post.find('script', type='application/ld+json').contents[0])
        name = data['name']
        price = data['']['offers']['price']
        floorSize = data['floorSize']
        csv_writer.writerow([name, price, floorSize])

# for post in posts:
#     print(post)



