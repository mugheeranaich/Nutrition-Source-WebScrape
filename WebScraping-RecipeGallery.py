from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.hsph.harvard.edu/nutritionsource/recipes-complete-list/'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

h1_tag = soup.find('h1')
title = h1_tag.text.strip()


os.mkdir(title)

h3_tags = soup.find_all('h3')
os.chdir(title)
for h3_tag in h3_tags:
    if 'style' not in h3_tag.attrs:
        folder = h3_tag.text.strip()
        os.mkdir(folder)
        print(folder)

        associated_li_tags = h3_tag.find_next_sibling('ul').find_all('li')
        os.chdir(folder)

        for li_tag in associated_li_tags:
            sub_folder = li_tag.text.strip()
            os.mkdir(sub_folder)
            href= li_tag.find('a')
            href_link = href.get('href')


            if href_link.startswith('%'):
                os.chdir(sub_folder)
                link = href_link.split('/')
                url = f'https://www.hsph.harvard.edu/nutritionsource/{link[1]}'
                response = requests.get(url)
                content = response.content
                soup = BeautifulSoup(content, 'html.parser')
                img_tag = soup.find('img')
                img = img_tag.get('src')
                os.system(f'wget "{img}" ')
                os.chdir('..')


            elif href_link.startswith('https') or href_link.startswith('hhttp'):
                os.chdir(sub_folder)
                url = href_link
                response = requests.get(url)
                content = response.content
                soup = BeautifulSoup(content, 'html.parser')
                img_tag = soup.find('img')
                img = img_tag.get('src')
                os.system(f'wget "{img}" ')
                os.chdir('..')


            elif href_link.startswith('recipes'):
                os.chdir(sub_folder)
                url = f'http://hsph.harvard.edu/nutritionsource/home-cooking/{href_link}'
                response = requests.get(url)
                content = response.content
                soup = BeautifulSoup(content, 'html.parser')
                img_tag = soup.find('img')
                img = img_tag.get('src')
                os.system(f'wget "{img}" ')
                os.chdir('..')


            else:
                os.chdir(sub_folder)
                url = href_link
                response = requests.get(url)
                content = response.content
                soup = BeautifulSoup(content, 'html.parser')
                img_tag = soup.find('img')
                img = img_tag.get('src')
                os.system(f'wget "{img}" ')
                os.chdir('..')


        os.chdir('..')
