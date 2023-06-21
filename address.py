import requests
from bs4 import BeautifulSoup
import mechanize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Array of links
links =  [
    "https://www.paychex.com/locations/arizona/phoenix",
    "https://www.paychex.com/locations/arizona/tempe",
    "https://www.paychex.com/locations/arizona/tucson",
    "https://www.paychex.com/locations/arkansas/little-rock",
    "https://www.paychex.com/locations/california/glendale",
    "https://www.paychex.com/locations/california/san-ramon",
    "https://www.paychex.com/locations/colorado/denver",
    "https://www.paychex.com/locations/connecticut/rocky-hill",
    "https://www.paychex.com/locations/florida/jacksonville",
    "https://www.paychex.com/locations/florida/lake-mary",
    "https://www.paychex.com/locations/florida/miramar",
    "https://www.paychex.com/locations/florida/sarasota",
    "https://www.paychex.com/locations/florida/st-petersburg",
    "https://www.paychex.com/locations/florida/west-palm-beach",
    "https://www.paychex.com/locations/illinois/chicago",
    "https://www.paychex.com/locations/indiana/indianapolis",
    "https://www.paychex.com/locations/iowa/des-moines",
    "https://www.paychex.com/locations/louisiana/baton-rouge",
    "https://www.paychex.com/locations/maine/auburn",
    "https://www.paychex.com/locations/maryland/owings-mills",
    "https://www.paychex.com/locations/massachusetts/auburn",
    "https://www.paychex.com/locations/michigan/novi",
    "https://www.paychex.com/locations/minnesota/eagan",
    "https://www.paychex.com/locations/new-jersey/mt-arlington",
    "https://www.paychex.com/locations/new-mexico/albuquerque",
    "https://www.paychex.com/locations/new-york/rochester",
    "https://www.paychex.com/locations/north-carolina/charlotte",
    "https://www.paychex.com/locations/north-carolina/high-point",
    "https://www.paychex.com/locations/ohio/dublin",
    "https://www.paychex.com/locations/ohio/franklin",
    "https://www.paychex.com/locations/oregon/beaverton",
    "https://www.paychex.com/locations/pennsylvania/allentown",
    "https://www.paychex.com/locations/tennessee/nashville",
    "https://www.paychex.com/locations/texas/irving",
    "https://www.paychex.com/locations/wisconsin/appleton",
]

# Array to store branch addresses
branch_addresses = []

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # You may need to adjust the webdriver based on your browser

# Loop through each link
for link in links:
    

    # Load the webpage
    driver.get(link) 
    print(link)

    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_all_elements_located((By.NAME, "container-12")))


    # # Get the page source
    page_source = driver.page_source
    # print(page_source)
    # Send a GET request to the link
    # response = requests.get(link)

    # chrome = mechanize.Browser()
    # chrome.set_handle_robots(False)
    # chrome.addheaders = [('User-agent', 
    # 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]
    # htmltext = chrome.open(link).read()
    
    # Parse the HTML content using BeautifulSoup

    # res = requests.post("https://geodis.com/us/geodis_custom_ajax_get_agency_popup",data="node_id="+link,headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"})

    soup = BeautifulSoup(page_source, "html.parser")
    # print(soup)
    
    # Find all div elements with class="branch__address"
    # street = soup.find("p",{"id": "ctl00_wpMngr_BranchDetail_BranchDetails_brAddress"})
    # street = soup.findAll("div", {"class":"information-section column"})
    street = soup.select(".information-section .left .columns div.column")
    soup2 = BeautifulSoup(str(street), "html.parser")
    streetinner = soup2.select(".column")
    
    # loca = soup.find("span",{"class": "locality"})
    # area = soup.find("span",{"class": "administrative-area"})
    # postal = soup.find("span",{"class": "postal-code"})

    streetData = streetinner[0].get_text(strip=True) if streetinner else ""
    # streetData = street[0].get_text(strip=True) if street else ""
    # locaData = loca.get_text(strip=True) if loca else ""
    # areaData = area.get_text(strip=True) if area else ""
    # postalData = postal.get_text(strip=True) if postal else ""

    print(streetData)
    if(street == None):
        print("None for ", link)
        continue
    
    # Extract the text from each address element and append it to the array
    # for address_element in street:
    branch_addresses.append(streetData)
    # branch_addresses.append(streetData+", "+locaData+", "+areaData+", "+postalData)
    # branch_addresses.append(street.get_text(strip=True))

# Print the array of branch addresses
print(branch_addresses)
