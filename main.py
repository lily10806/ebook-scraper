from scraper import *
from fileHandler import *
from tqdm import tqdm
from os import remove
import xml2epub

def main():
    URL = input('Enter URL to book: ')
    BOOKS_DIRNAME = 'books'

    # create driver
    driver = createDriverInstance()

    # create directory to store epub if not exist
    createDir(BOOKS_DIRNAME)

    # scrape website for title and chapters
    print('Getting info...')
    bookInfo = getInfo(driver, URL)
    title = bookInfo['title']
    author = bookInfo['author']
    chaptersLinks = bookInfo['chapters']

     # create empty ebook
    book = xml2epub.Epub(title, creator=author, language='vi')
    # create custom cover image
    coverImage = input('Enter link to custom cover image. Leave blank to generate default cover: ')
    print('Creating cover page...')
    cover = xml2epub.create_chapter_from_string(coverImage, title='cover', strict=False)
    book.add_chapter(cover)

    # get content for all chapters
    print('Creating EPUB...')
    for index, name in enumerate(tqdm(chaptersLinks, ascii='░▒█', ncols=100)):
        link = chaptersLinks[name]
        filename = f'{BOOKS_DIRNAME}/{index+1}.html'
        # get chapter's content and clean up HTML
        content = cleanContent(getContent(driver, link), name)
        # write to HTML file
        writeHTML(content, filename)
        # create chapter object from HTML file
        chapter = xml2epub.create_chapter_from_file(filename, strict=False)
        # add chapter to book
        book.add_chapter(chapter)
        # remove HTML file
        remove(filename)

    driver.quit() # quit browser driver
    # generate epub file
    book.create_epub(BOOKS_DIRNAME)
    print('EPUB file ready!')

if __name__ == '__main__':
    main()