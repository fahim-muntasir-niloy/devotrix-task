import requests, xml
from bs4 import BeautifulSoup
from selenium import webdriver




def fetch_latest_xml(url):
    browser = webdriver.Edge()
    
    browser.get(url)
    response_html = browser.page_source
    soup = BeautifulSoup(response_html, "html.parser")

    xml_links = []
    for link in soup.find_all('a'):
        if str(link.get('href')).endswith('xml'):
            xml_links.append(str(link.get('href')))
            
    return xml_links[-1]