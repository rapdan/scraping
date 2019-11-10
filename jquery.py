import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):                  #pobiera kod html strony
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gesko) Chrome/63.0.3239.132 Safari/537.36'}
    #niektóre strony odrzucają zapytania bez informacji o nagłówkach, dlatego w request dodano nagłówek
    r = requests.get(url, header=user_agent)
    return r.text

def write_csv(data):                #zapis danych do pliku .csv
    with open('testimonials.csv', 'a') as f:
        order = []
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_articles(html):             #wyszukuje artykuły
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts       #może zwrócić [a, b, c] lub [] jeżeli dojdzie do końca

def get_page_data(ts):              #szuka w artykułach autora, rok..
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since')
        except:
            since = ''
        try:
            author = t.find('p', c)
        except:
            author = ''
        data = {'author': author, 'since': since}
        write_csv(data)


def main():
    #1. Pobranie containera z opiniami
    #2. Jeżeli jest lista to parsujemy
    #3. Jeżeli lista jest pusta to cykl zostaje przerwany
    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page))

        articles = get_articles(get_html(url))  # [] or [1, 2, 3] pobranie artykułów
        if articles:
            get_page_data(articles)             #rozczłonkowanie każdego artykułu na dane
            page = page + 1                     # przejście do następnej strony
        else:
            break                               #break jeżeli nie ma więcej artykułów na stronie


if __name__ == '__main__':
    main()        
