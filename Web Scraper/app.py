import requests
import csv
from bs4 import BeautifulSoup
# URL = "https://www.fiverr.com/search/gigs?query=app%20script"
# html = requests.get(URL)
with open('content.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
soup = BeautifulSoup(html_content, 'html5lib')
gigs = soup.find_all('div', class_='gig-card-layout')

with open("gigs.csv", "w") as f:
    csv_file = csv.writer(f)
    csv_file.writerow(
        ['Link', 'Title', 'Image', 'Profile Picture', 'Ratings', 'Price'])
    for gig in gigs:
        gig_link = "https://www.fiverr.com" + gig.find('a').get('href')
        gig_title = gig.find('h3').text
        player = gig.find('div', class_='slide-item')
        gig_image = player.find('img').get('src') if player else ""
        seller = gig.find('div', class_='seller-info')
        pro_pic = seller.find('img').get('src')if seller else ""
        gig_rating = gig.find('span', class_='gig-rating')
        ratings = gig_rating.find('span').text.replace(
            "(", "").replace(")", "") if gig_rating else ""
        price = gig.find('footer').find('a').find('span').text.replace("$", "")
        csv_file.writerow(
            [gig_link, gig_title, gig_image, pro_pic, ratings, price])
