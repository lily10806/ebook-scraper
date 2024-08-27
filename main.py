from scraper import *
from fileHandler import *

# scrape website & clean content
content = cleanContent(getContent())
# write to html file
writeHTML(content)