from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

DELAY = 5

def createDriverInstance():
    chromeOptions = Options()
    chromeOptions.add_argument('--headless=new')
    chromeOptions.add_argument('--headless')
    driver = webdriver.Chrome(options=chromeOptions)
    return driver

def getChapters(driver, url):
    driver.get(url)
    try:
        elements = WebDriverWait(driver, DELAY).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#list-chapter .list-chapter li a"))
        )
        chaptersLinks = {el.text : el.get_attribute('href') for el in elements}
        print(f'Chapters discovered: {len(chaptersLinks)}')
        return chaptersLinks
    except:
        print('An error has occured')

def getContent(driver, url):
    driver.get(url)
    try:
        element = WebDriverWait(driver, DELAY).until(
            EC.presence_of_element_located((By.ID, "chapter-c"))
        )
        content = element.get_attribute('innerHTML')
        return str(content)
    except:
        print('An error has occured')

def cleanContent(content, chapName):
    content = f'\
        <!DOCTYPE html>\
        <html>\
            <head>\
                <title>{chapName}</title>\
            </head>\
            <body>\
                <h1>{chapName}</h1>\
                <p>{content}</p>\
            </body>\
        </html>'
    elements = ['script', 'div', 'em']
    # parse html
    soup = BeautifulSoup(content, 'html.parser')
    # loop through all unwanted elements
    for el in elements:
        # remove all specific elements from html
        for s in soup.find_all(el):
            s.decompose()
    return soup.prettify()

def prettifyHTML(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.prettify()