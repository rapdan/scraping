#Skrypt do scrapingu kanału youtube

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r                                #tym razem zwraca r

def write_csv(data):                        #zapis danych do pliku csv
    with open('videos.csv', 'a') as f:
        order = ['name', 'url']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:  
        html = response.text                        #pierwsza strona youtube zwraca html
    else:
        html = response.json()['content_html']      #następne strony zwracają objekt json

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('h3', class_='yt-lockup-title')   #pobranie informacji o filmach

    for item in items:
        name = item.text.strip()                #wydzielenie tytułu
        url = item.find('a').get('href')        #wydzielenie linka

        data = {'name': name, 'url': url}
        write_csv(data)


def get_next(response):                         #określa następne adresy stron z filmami dla tego samego kanału
    if 'html' in response.headers['Content-Type']:
        html = response.text                    
    else:
        html = response.json()['load_more_widget_html']

    soup = BeautifulSoup(html, 'lxml')

    try:
        url = 'https://youtube.com' + soup.find('button', class_='load-more-button').get('data-uix-load-more-href')
    except:
        url = ''

    return url


def main():
    # url = 'https://www.youtube.com/browse_ajax?action_continuation=1&direct_render=1&continuation=4qmFsgJAEhhVQ09tNF9BbkxQTEVCVnJiby0tTjdrUEEaJEVnWjJhV1JsYjNNZ0FEZ0JZQUZxQUhvQk1yZ0JBQSUzRCUzRA%253D%253D'
    url = 'https://www.youtube.com/user/coolpropaganda/videos'
    # get_page_data(get_html(url))

    while True:                #główna pętla
        response = get_html(url)
        get_page_data(response)

        url = get_next(response)

        if url:
            continue
        else:
            break           #jeżeli url pusty






if __name__ == '__main__':
    main()