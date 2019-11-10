import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):          #definicja funkcji zwracającej tekst html-a
    r = requests.get(url)   #r posiada metody dir(r)
    return r.text           #jedna z metod r.text zwraca cały tekst strony

def get_data(html):         #funkcja wyszukuje w tekscie html nagłówek h1
    soup = BeautifulSoup(html, 'lxml') #dir(soup)
    #h1 = soup.find('h1')
    #h1 = soup.find('header', id='page-hero').find('h1').text
    s = soup.find('section', class_="layout-media container my-5").find_all('section')[1] 
                                                            #find_all znajduje wszystkie elementy
                                                            # i zwraca listę. [1] wybiera drugi element listy
    all_section = soup.find('section', class_="layout-media container my-5").find_all('section')
    for one_section in all_section:
        name = one_section.find('h4').text  
        #print(name)
        tekst = one_section.find('p').text  
        #print(tekst)
        data = {
            'name': name,
            'paragraf': tekst
        }
        print(data)
        write_csv(data)
    urll = all_section[2].find('a').get('href') #zwracanie linków: https://www.facebook.com/pg/100pacom/reviews/
    print(urll)
    urln = all_section[2].find('a').text        #zwracanie tekstu do linków:  Link do facebook.
    print(urln)
    #return s

def get_data2(html):                     #funkcja scrapuje tablice do pliku.csv
    soup = BeautifulSoup(html, 'lxml')  #utworzenie obiektu, klasy BeautifulSoup
    trs = soup.find('table', id='currencies').find('tbody').find_all('tr') # tworzy listę wszystkich kryptowalut
                                        #odnajduje tabele i jej tbody. Zwraca wszystkie rzędy tabeli: tr 
    for tr in trs:
        tds = tr.find_all('td')         #tworzymy listę danych dla danej kryptowaluty
        name = tds[1].find('a', class_='currency-name-container').text 
                                        #nazwa kryptowaluty znajduje sie na drugim miejscu w liście, pierwszym jest numer porzadkowy
        symbol = tds[1].find('a').text  #na stronie znajduje się ukryty symbol kryptowaluty
        url = 'https://coinmarketcap.com'+tds[1].find('a').get('href')  #grabimy linka do danej kryptowaluty (podlinkowana nazwa)
        price = tds[3].find('a').get('data-usd')
        data = {'name': name, 'symbol': symbol, 'url': url, 'price': price}
        write_csv(data)

def write_csv(data):               #zapisuje dane do pliku.csv
    with open('plik.csv', 'a') as f:
        writer = csv.writer(f)
        #writer.writerow((data['name'], data['paragraf']))
        writer.writerow((data['name'], data['symbol'], data['url'], data['price']))


def refined(linia):
    #funkcja zamienia '182,889 total ratings' na 182889
    r = linia.split(' ')[0]
    return r.replace(',', '')



def main():
    #url = 'https://100pa.com'
    url2 = 'https://coinmarketcap.com'
    #print(get_data(get_html(url)))
    print(get_data2(get_html(url2)))

if __name__ == '__main__':
    main()