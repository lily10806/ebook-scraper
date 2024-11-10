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
    chromeOptions.add_argument('--ignore-certificate-errors')
    chromeOptions.add_argument('--ignore-ssl-errors')
    chromeOptions.add_argument('--log-level=2')
    driver = webdriver.Chrome(options=chromeOptions)
    return driver

def getInfo(driver, url):
    try:
        driver.get(url)

        # get book's title
        title = WebDriverWait(driver, DELAY).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
        ).text.title()
        # get author
        author = WebDriverWait(driver, DELAY).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".info a[itemprop='author']"))
        ).text.title()
        print(author)
        # get list dictionary of chapters' names and links
        chapters = WebDriverWait(driver, DELAY).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#list-chapter .list-chapter li a"))
        )
        chaptersLinks = {c.text : c.get_attribute('href') for c in chapters}
        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f'Number of Chapters: {len(chaptersLinks)}')
        bookInfo = {
            'title' : title,
            'author': author,
            'chapters': chaptersLinks
        }
        return bookInfo
    except:
        print('An error has occured')

def getContent(driver, url):
    try:
        driver.get(url)
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
                <h1 style="text-align:center;">{chapName}</h1>\
                <p>{content}</p>\
            </body>\
        </html>'
    elements = ['script', 'div', 'em', 'a', 'img']
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