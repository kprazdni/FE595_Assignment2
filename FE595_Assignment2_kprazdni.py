# Katelin Prazdnik
# FE595 Assignment 2 - Webscraper
# October 6, 2020
# I pledge on my honor that I have not given or received any unauthorized assistance on
# this assignment/examination. I further pledge that I have not copied any material from
# a book, article, the Internet or any other source except where I have expressly cited the
# source.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
def get_HTML(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def extract_line(header,soup):
    return re.findall('%s: +(.*)' %(header),soup.get_text())[0]

def save_info(soup,df=pd.DataFrame()):
    name = extract_line('Name',soup)
    purpose = extract_line('Purpose',soup)
    return df.append(pd.Series({'Name':name,'Purpose':purpose}),ignore_index=True)



if __name__ == "__main__":
    url = 'http://3.95.249.159:8000/random_company'
    output = pd.DataFrame()
    for i in range(50):
        soup = get_HTML(url)
        output = save_info(soup,df=output)
    output.to_csv('RandomCompanyExport.csv')

