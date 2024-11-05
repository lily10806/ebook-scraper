import os
def createDir():
    try:
        print('Creating directory for chapters')
        os.makedirs('chapters')
    except:
        print('Directory for chapters already exist')

def writeHTML(content):
    # open html file
    createDir()
    with open('chapters/chapter.html', 'w', encoding='utf-8') as f:
        f.write(content)