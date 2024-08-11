from fetch_latest_xml import fetch_latest_xml
from xml_to_pdf import xml_to_pdf



def main(site_link = "https://www.govinfo.gov/bulkdata/CFR/2024/title-12"):
    
    latest_xml = fetch_latest_xml(site_link)
    print(f"Found latest XML file at: {latest_xml}. Conversion started.")
    
    xml_to_pdf(site_link, latest_xml)
    print(f"{latest_xml.split('/')[-1]} converted to PDF and saved.")



if __name__ == "__main__":
    main()