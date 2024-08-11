import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import urljoin
import pdfkit


def xml_to_pdf(url, xml_link):

    file_path = urljoin(url, xml_link)
    xml_res = requests.get(file_path)
    file = BeautifulSoup(xml_res.content, "lxml-xml")
    html_content = file.prettify()
    
    pdfkit.from_string(html_content, "output1.pdf")
    
    
