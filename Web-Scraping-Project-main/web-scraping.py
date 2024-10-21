from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

data= pd.read_csv("data.csv")

for i in range(1000):
    Asin = data.Asin[i]
    asin = Asin.replace("'", "")
    Country = data.country[i]
    country = Country.replace("'", "")
    URL = 'https://www.amazon.{}/dp/000{}'.format(country,asin)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    if(soup1.find(id='productTitle') == None):
        continue
    
    title = soup1.find(id='productTitle').get_text()

    if(soup1.find('span', 'a-offscreen') == None):
        price = "Price Unavailable"
    else:
        price = soup1.find('span', 'a-offscreen').text

    if(soup1.find(id = "imgBlkFront")== None):
        image = "Image Unavailable"
    else:
        image = soup1.find(id = "imgBlkFront")['src']

    if (soup1.find(id = "detailBullets_feature_div") == None):
        details = "No Details"
    else: 
        details1 = soup1.find(id = "detailBullets_feature_div")
        if (details1.ul == None):
            details = "No Details"
        else:
            details2 = details1.ul.text
            details = " ".join(details2.split())
    
    dict = {'Title':title, 'Price':price, 'Image_URL':image, 'Details':details}
    
    def write_json(new_data, filename='data.json'):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["all_data"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    
    write_json(dict)