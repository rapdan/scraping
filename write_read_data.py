import csv


def write_csv(data):                                    #zapis jako lista
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['surname'], data['age']))


def write_csv2(data):                                   #zapis jako słownik
    with open('names.csv', 'a') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)




def main():
    d = {'name': 'Piotr', 'surname': 'Kowalski', 'age': 21}
    d1 = {'name': 'Adam', 'surname': 'Ivanov', 'age': 18}
    d2 = {'name': 'Ksu', 'surname': 'Petros', 'age': 32}

    l = [ d, d1, d2 ]


    with open('cmc.csv') as file:                       #odczyt danych z cmc.csv
        fieldnames = ['name', 'url', 'price']           #przyporządkowanie nagłówków do danych
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
