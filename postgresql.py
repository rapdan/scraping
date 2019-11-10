#sudo apt install postgresql pgadmin3
#Po instalacji logowanie do programu aby zmieni© hasło:
#sudo -u postgres psql
#\password                  #zmiana hasła
#CREATE DATABASE test;      #utworzenie bazy: test
#\l                         #wyświetlenie baz danych
#\q                         #wyjscie z bazy danych
#pg_dump -U postgres -h localhost test > coins.sql      #dump bazy test do pliku coins.sql

#sudo pip3 install peewee psycopg2 psycopg2-binary      #instalacja do obsługi baz i postgresql



import csv
from peewee import *

db = PostgresqlDatabase(database='test', user='postgres', password='1', host='localhost')


class Coin(Model):
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db



def main():

    db.connect()
    db.create_tables([Coin])

    with open('cmc.csv') as f:
        order = ['name', 'url', 'price']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        # for row in coins:
            # coin = Coin(name=row['name'], url=row['url'], price=row['price'])
            # coin.save()

        with db.atomic():
            # for row in coins:
            #     Coin.create(**row)
            for index in range(0, len(coins), 100):
                Coin.insert_many(coins[index:index+100]).execute()


if __name__ == '__main__':
    main()