import requests
from bs4 import BeautifulSoup

logo_urls = []

# scrape first website

url1 = "https://webflow.com"

page1 = requests.get(url1)

soup1 = BeautifulSoup(page1.text, features="html.parser")
divs1 = soup1.find_all("div", {"class": "intro-logos_wrapper"})

for div in divs1:
    for element in div.find_all("img"):
        pic_url = element["src"]
        brand_name = element["alt"].replace("logo", "")
        brand_dict = {brand_name.upper(): pic_url}

        if brand_dict not in logo_urls:  # avoid adding duplicates
            logo_urls.append(brand_dict)

# scrape second website

url2 = "https://scale.com"

page2 = requests.get(url2)

soup2 = BeautifulSoup(page2.text, features="html.parser")

lis = soup2.find_all("li", {"class": "flex justify-center items-center"})
for li in lis:
    for element in li.find_all("img"):
        pic_url = element["src"]
        brand_name = element["alt"].replace("logo", "").replace("-", " ")
        brand_dict = {brand_name.upper(): url2 + pic_url}
        logo_urls.append(brand_dict)

# scrape third website

url3 = "https://www.deel.com"

page3 = requests.get(url3)

soup3 = BeautifulSoup(page3.text, features="html.parser")

divs3 = soup3.find_all(
    "div", {"class": ["scroll-looper-sec", "slick-initialized", "slick-slider"]}
)

for div in divs3:
    for element in div.find_all("img"):
        pic_url = element["src"]
        brand_name = element["alt"]
        cleaned_name = (
            brand_name.lower().replace("-", " ").replace("_", " ").replace(".", " ")
        )
        extra_strings = [
            "white",
            "logo",
            "1",
            "2019",
            "2016",
            " ",
        ]  # clean brand name by removing unnecessary strings
        final_brand_name = " ".join(
            [x for x in cleaned_name.split() if x not in extra_strings]
        )
        brand_dict = {final_brand_name.upper(): pic_url}

        logo_urls.append(brand_dict)

# write image urls to file

multiline_string = "".join(
    [
        name + ": " + url + "\n"
        for logo_url in logo_urls
        for name, url in logo_url.items()
    ]
)  # create a multiline string from dict of image

text_file = open("image_urls.txt", "w")
text_file.write(multiline_string)
text_file.close()
