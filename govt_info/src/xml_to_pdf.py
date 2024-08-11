import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import urljoin
import pdfkit


def xml_to_pdf(url, xml_link):
    """Convert xml file to readable PDF
    
    Keyword arguments:
    url -- base website
    xml_link -- xml file url, from `fetch_latest_xml` function
    Return: saves a PDF file
    """
    

    file_path = urljoin(url, xml_link)  # creating url of latest xml file
    xml_res = requests.get(file_path)
    
    file = BeautifulSoup(xml_res.content, "lxml-xml")   # using lxml parser for faster result
    html_content = file.prettify()
    
    pdfkit.from_string(html_content, "output2.pdf")
    
    
