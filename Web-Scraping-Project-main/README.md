# Web-Scraping-Project
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AnshChoudhary/Web-Scraping-Project/blob/main/web-scraping.ipynb#scrollTo=Dqv4-oc-q26n)  <br />
Python program to scrape 1000 websites using Beautiful Soup 4. <br />
In this task we want you to scrape a minimum hundred URLs.
The URL will be in format of "https://www.amazon.{country}/dp/{asin}".
The country code and Asin parameters are in the CSV file 
https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit?usp=sharing . The CSV file contains 1000 
rows. <br /><br />
Use Selenium or bs4 to Scarpe the following details from the page.<br />
1. Product Title <br />
2. Product Image URL <br />
3. Price of the Product <br />
4. Product Details <br /> <br />
If any URL throws Error 404 then print the {URL} not available and skip 
that URL.

## Instructions
1. Run the web-scraping.py file to extract data (asin and country) from the data.csv file and looping it through the scrapting process to output the results to the data.json file.
2. captcha.py is the BONUS task that solves the captcha on https://www.amazon.com/errors/validateCaptcha and submits the form successfully.
3. You can also access the web-scraping.py program on Google Collab using the Google Collab button at the beginning of this README.

## Feedback 
For every batch of 100 websites, the program took 2 minutes and 21 seconds on average.

## Thank you 
I would also like to attach <a href="https://ansh-portfolio.web.app/">my portfolio website link</a> which I designed and coded myself. 


