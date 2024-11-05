import os
# function to create directory to store files if not found
def createDir(dirname):
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

# function to write HTML content into HTML files
def writeHTML(content, filename):
    # open and write in html file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)