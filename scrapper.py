from bs4 import BeautifulSoup
import requests


def get_links(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')

    links = []
    for link in soup.find_all('a'):
        link_url = link.get('href')

        if link_url is not None and link_url.startswith('http'):
            links.append(link_url + '\n')

    write_to_file(links)
    return links


def write_to_file(links):
    with open('data.txt', 'a') as f:
        f.writelines(links)


def get_all_links(url):
    for link in get_links(url):
        get_all_links(link)


r = '127.0.0.1:8000/.hidden'
write_to_file([r])
get_all_links(r)