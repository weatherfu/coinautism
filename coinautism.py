# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
outputfile = open('output.txt', 'w')
s = requests.Session()
s.mount('https://', HTTPAdapter(max_retries=5))
urls = ['https://www.changechecker.org/search-results.aspx?denominationId=1&subcategory=Year&subcategoryId=1000','https://www.changechecker.org/search-results.aspx?denominationId=3&subcategory=Year&subcategoryId=1000', 'https://www.changechecker.org/search-results.aspx?denominationId=4&subcategory=Sport&subcategoryId=1010', 'https://www.changechecker.org/search-results.aspx?denominationId=15&subcategory=Letter&subcategoryId=-1', 'https://www.changechecker.org/search-results?denominationId=9&subcategory=Year&subcategoryId=1000', 'https://www.changechecker.org/search-results.aspx?denominationId=16&subcategory=Definitive&subcategoryId=1020', 'https://www.changechecker.org/search-results.aspx?denominationId=7&subcategory=Year&subcategoryId=1000', 'https://www.changechecker.org/search-results.aspx?denominationId=5&subcategory=Year&subcategoryId=1000', 'https://www.changechecker.org/search-results.aspx?denominationId=2&subcategory=Year&subcategoryId=1000', 'https://www.changechecker.org/search-results.aspx?denominationId=6&subcategory=Year&subcategoryId=1000']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
}
for url in urls:
    urldata = s.get(url, headers=headers)
    soup = bs(urldata.text,'html.parser')
    elements = soup.find_all('div', class_='divCoinBackground')
    coinlinks = []
    for element in elements:
        coinlink = 'https://www.changechecker.org/' + element.a['href']
        coinlinks.append(coinlink)
    for coinlink in coinlinks:
        coindata = s.get(coinlink, headers=headers)
        coinsoup = bs(coindata.text, 'html.parser')
        try:
            cointitle = coinsoup.find('span', id='ContentPlaceHolderBodyText_ctl00_coin-details_1_lblCoinTitle').text.encode('utf-8')
        except:
            cointitle = ''
        try:
            mintage = coinsoup.find('h2', text='Circulating mintage: ').next_element.next_element.text
        except:
            mintage = ''
        try:
            years = coinsoup.find('span', id='ContentPlaceHolderBodyText_ctl00_coin-details_1_lbl_years').text
        except:
            years = ''
        try:
            rarity = coinsoup.find('span', id='ContentPlaceHolderBodyText_ctl00_coin-details_1_scarcityIndexBandLabel').text
        except:
            rarity = ''
        if cointitle:
            print cointitle
            outputfile.write(cointitle + '\n')
        if mintage:
            print mintage
            outputfile.write(mintage + '\n')
        if years:
            print years
            outputfile.write(years + '\n')
        if rarity:
            print rarity
            outputfile.write(rarity + '\n')
        print '---'

outputfile.close()