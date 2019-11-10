#Skrypt wykonuje parsing w kilku procesach na raz

import requests
import csv
from multiprocessing import Pool
from time import sleep

def get_html(url):                              #funkcja pobiera tekst ze stony
    # sleep(1)                                  #czasami trzeba spowolnić parsing ,aby nie zbanowali
    r = requests.get(url)
    return r.text


def write_csv(data):                            #funkcja zapisująca dane do pliku .csv
    with open('websites.csv', 'a') as file:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_page_data(text):
        data = text.strip().split('\n')[1:]     #przekazanie tekstu podzielonego na linie '\n'
                                                #z obcięciem białych znaków strip()
                                                #i odrzuceniem pierwszego elementu z indexem [0]

        for row in data:
            columns = row.strip().split('\t')   #rozdzielenie linii na elementy po tabulacji '\t'
            name = columns[0]                   #przypisanie kolejnym elementom nazw
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,               #przygotowanie danych do zapisu
                    'url': url,                 #dane muszą być jednakowe z nagłówkiem (order) w funkcji write_csv
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            write_csv(data)                     #zapis danych do pliku


def make_all(url):                              #funkcja parsująca pojedyńczą stronę
    text = get_html(url)
    get_page_data(text)


def main():                                     #główna funkcja
    #do parsowania jest 6320 adresow


    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'    #pattern
    urls = [url.format(str(i)) for i in range(1, 6321)]                 #generacja listy adresów

    with Pool(20) as p:                         #Z biblioteki Pool można stworzyć jakby 20 pracowników
        p.map(make_all, urls)                   #map przyjmuje jako argumenty: funkcję i listę zadań
                                                #nazwę funkcji podaje się bez nawiasów




if __name__ == '__main__':
    main()
