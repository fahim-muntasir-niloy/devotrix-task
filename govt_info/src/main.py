from fetch_latest_xml import fetch_latest_xml
from xml_to_pdf import xml_to_pdf


site_link = "https://www.govinfo.gov/bulkdata/CFR/2024/title-12"

def main():
    latest_xml = fetch_latest_xml(site_link)
    print(latest_xml)
    xml_to_pdf(site_link, latest_xml)
    print(f"PDF saved")



if __name__ == "__main__":
    main()