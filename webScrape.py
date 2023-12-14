#! Python3 - webScraping

import requests, bs4

# Example site - https://text.npr.org/
# Selector - li

def getWebsite(urlAddress):
    
    res = requests.get(urlAddress) # downloads and saves the HTML in a var called res as a text
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    cssSelector = input('Please enter the CSS Element you want: ')
    elems = soup.select(cssSelector) # CSS ELEMENT THAT YOU WANT *Using Chrome - Copy Selector
    
    return elems[0].text.strip()

url2scrape = input('Please enter the URL you want to scrap: ')
data = getWebsite(url2scrape)
print('Here is the data you requested:' + data)
