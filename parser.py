import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

# Config
count = 0
urls = ['https://en.wikipedia.org/wiki/Web_scraping',
        'https://en.wikipedia.org/wiki/Data_scraping',
        'https://en.wikipedia.org/wiki/Computer_program',
        'https://en.wikipedia.org/wiki/Execution_(computing)',
        'https://en.wikipedia.org/wiki/Session_(computer_science)']

# CSV Config
file = open('data.csv', 'w', encoding='utf-8')
writerobj = csv.writer(file)
writerobj.writerow(['Page Count', 'Url', 'Info'])

for url in urls:
    count += 1
    element_Text_ls = []
    result = ''

    page_HTML = requests.get(url).text
    page = BeautifulSoup(page_HTML, 'html.parser')

    content_Block = page.find('div', {'class': 'mw-parser-output'})
    for element in content_Block.find_all():
        if element.name == 'h2':
            if element.span.text in ['See also', 'References']:
                break

        elif element.name == 'p':
            print(element.findParent().name)
            element_Text_ls.append(element.text)

        elif element.name == 'ul':
                print(element.findParent().name)
                element_Text_ls.append(element.text)

    for element in element_Text_ls:
        result += element

    print(f'\n\n------- Page {count} -------\n')
    print(result)

    writerobj.writerow([count, url, result])
    print(f'Successfully saved page {count} content. Waiting for request cooldown!')

    sleep(10)

file.close()
print('Finished!')
