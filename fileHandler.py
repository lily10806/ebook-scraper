import os
def createDir():
    try:
        os.makedirs('chapters')
        print('Directory created')
    except:
        print('Directory for chapters already exist')

def writeHTML(content, filename):
    # open and write in html file
    with open(f'chapters/{str(filename)}.html', 'w', encoding='utf-8') as f:
        f.write(content)