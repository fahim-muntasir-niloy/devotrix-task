# devotrix-task

## Project Summary
This repo contains code to perse xml urls from a site, and then converts the last/latest xml file to pdf.

## Tools
I have used Selenium, BeautifulSoup, PDFkit and LXML in different parts of the project.

Naive BeautifulSoup html perser struggled to extract `a tags` from nested divs. So, Selenium webdriver was used to create better html structure. BS4 was then able to extract the necessary files. To parse `XML`, lxml parser was used with BS4 for faster performance.  

PDFKit converted the extracted XML to a PDF file, with the help of [[wkhtmltopdf](https://wkhtmltopdf.org/)]. It was setup on the machine locally.

- how to run this project