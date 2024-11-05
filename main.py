from scraper import *
from fileHandler import *
from tqdm import tqdm

def main():
    URL = "https://truyenfull.io/thoi-nien-thieu-tuoi-dep-ay/"
    # create driver
    driver = createDriverInstance()
    # scrape website & clean content
    print('Getting chapters...')
    chaptersLinks = getChapters(driver, URL)
    # create directory to store chapters
    print('Creating directory for chapters')
    createDir()
    print('Getting content...')
    for index, name in enumerate(tqdm(chaptersLinks, ascii='░▒█', ncols=100)):
        link = chaptersLinks[name]
        # get chapter's content and clean up HTML
        content = cleanContent(getContent(driver, link), name)
        # write to html file
        writeHTML(content, index + 1)
    print('HTML files ready!')

if __name__ == '__main__':
    main()