import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:                #jeżeli nie zbanowali nas to odpowiedź 200
        return r.text
    print(r.status_code)

def refine_cy(s):                   #formatuje do liczby ranking
    return s.split(' ')[-1]

def write_csv(data):                #zapisuje dane do pliku
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['url'], data['snippet'], data['cy']))

def get_page_data(html):                                #przebiega po elementach listy
    soup = BeautifulSoup(html,'lxml')                   #i zbiera dane:
    lis = soup.find_all('li', class_='yaca-snippet')
    for li in lis:
        try:
            name = li.find('h2').text                   #naglówek
        except:
            name = ''

        try:
            url = li.find('h2').find('a').get('href')   #link do strony
        except:
            url = ''

        try:
            snippet = li.find('div', class_='yaca-snippet__text').text.strip() #opis strony
        except:
            snippet = ''

        try:
            c = li.find('div', class_='yaca-snippet__cy').text.strip()
            cy = refine_cy(c)
        except:
            cy = ''

        data = {                    #tworzymy linie danych jako słownik
            'name': name,
            'url': url,
            'snippet': snippet,
            'cy': cy
        }

        write_csv(data)             #zapis linii do pliku .csv

def main():
    # pattern = 'https://yandex.ru/yaca/cat/Entertainment/{}'
    # for i in range(0,10):
    #     url = pattern.format(i)
    #     get_page_data(get_html(url))
    url = 'https://coinmarketcap.com/'

    while True:                         #Pętla dopóki istnieją strony
        get_page_data(get_html(url))    #Pobierz dane z bierzącej strony
        soup = BeautifulSoup(get_html(url), 'lxml' )    #Ponowne tworzenie soup dla utworzenia adresu nastepnej strony
        try:
            pattern = 'Next'
            url = 'https://coinmarketcap.com/' + soup.find('ul', class_='pagination').find('a',
            text=re.compile(pattern)).get('href')       #skorzystanie z regulanego wyrażenia any znaleźć słowo: Next
        except:
            break                       #Break jeżeli brak następnej strony




if __name__ == '__main__':
    main()