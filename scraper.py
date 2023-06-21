import requests
from bs4 import BeautifulSoup

url = 'https://webflow.com'

page = requests.get(url)

soup = BeautifulSoup(page.text, features='html.parser')
divs = soup.find_all("div", {"class": "intro-logos_wrapper"})
for div in divs:
    for element in div.find_all("img"):
        pic_url = element['src']
        # print(pic_url)


#second page        

# url2 = 'https://scale.com'

# page2 = requests.get(url2)

# soup2 = BeautifulSoup(page2.text, features='html.parser')

# lis = soup2.find_all("li", {"class": "flex justify-center items-center"})
# for li in lis:
#     for element in li.find_all("img"):
#         pic_url = element.get("src")
#         print(url2 + pic_url)

# with open('test.svg', 'w') as file:
#     data = requests.get('https://scale.com/_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fetsy.svg&w=96&q=100').text
#     file.write(data)

#third page

url3 = 'https://www.deel.com'

page3 = requests.get(url3)

soup3 = BeautifulSoup(page3.text, features='html.parser')
# print(soup3)

# divs3 = soup3.find_all("div", {'class': ['single-image', 'slick-slide', 'slick-cloned', 'logo-scroll-looper']})

divs3 = soup3.find_all("div", {'class': ['scroll-looper-sec',  'slick-initialized', 'slick-slider']})
# print(divs3)
for div in divs3:
    for element in div.find_all("img"):
        pic_url = element['src']
        print(pic_url)

