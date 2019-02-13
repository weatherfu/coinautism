from bs4 import BeautifulSoup as bs
import requests
urls = ['https://www.changechecker.org/search-results.aspx?denominationId=1&subcategory=Year&subcategoryId=1000','https://www.changechecker.org/search-results.aspx?denominationId=3&subcategory=Year&subcategoryId=1000', 'https://www.changechecker.org/search-results.aspx?denominationId=4&subcategory=Sport&subcategoryId=1010', 'https://www.changechecker.org/search-results.aspx?denominationId=15&subcategory=Letter&subcategoryId=-1']
for url in urls:
    urldata = requests.get(url)
    soup = bs(urldata.text,'html.parser')
    elements = soup.find_all('div', class_='divCoinBackground')
    coinlinks = []
    for element in elements:
        coinlink = 'https://www.changechecker.org/' + element.a['href']
        coinlinks.append(coinlink)
    for coinlink in coinlinks:
        coindata = requests.get(coinlink)
        coinsoup = bs(coindata.text, 'html.parser')
        try:
            cointitle = coinsoup.find('span', id='ContentPlaceHolderBodyText_ctl00_coin-details_2_lblCoinTitle').text
        except:
            cointitle = ''
        try:
            mintage = coinsoup.find('h2', text='Mintage: ').next_element.next_element.text
        except:
            mintage = ''
        try:
            years = coinsoup.find('span', id='ContentPlaceHolderBodyText_ctl00_coin-details_2_lbl_years').text
        except:
            years = ''
        try:
            rarity = coinsoup.find('span', id='ContentPlaceHolderBodyText_ctl00_coin-details_2_scarcityIndexBandLabel').text
        except:
            rarity = ''
        if cointitle:
            print cointitle
        if mintage:
            print mintage
        if years:
            print years
        if rarity:
            print rarity
        print '---'
