#.find()                    szuka pierwsze wystąpienie danego elementu
#.find_all()                szuka wszystkie wystąpienia elementów
#.get('href')               szuka linku
#.text                      szuka div-u w którym jest określony dany tekst 
#.parent                    szuka div-u rodzicielskiego np. alena = soup.find('div', text='Alena').parent
#.find_parent(class_='row') szuka div-u rodzicielskiego, ale z class = 'row'
#.parents
#.find_parents
#.find_next_sibling()       szuka następnego elementu bliźniaczego
#.find_previous_sibling     szuka wcześniejszego elementu bliźniaczego

#{'sal': 'salery'}          szuka np. <div sal="salery>200$</div>"
#regularne wyrażenia pythex.org


def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def get_salary(s):
    # salary: 2700 usd per month
    pattern = r'\d{1,9}'
    # salary = re.findall(pattern, s)[0]
	# salery = re.search(pattern, s).group()
    print(salary)


def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')
    # row = soup.find_all('div', {'data-set': 'salary'})
    #
    # alena = soup.find('div', text='Alena').find_parent(class_='row')
    # print(alena)

    # copywriters = []
    #
    # persons = soup.find_all('div', class_='row')
    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append(cw)
    #
    # print(copywriters)

    salary = soup.find_all('div', text=re.compile('\d{1,9}'))
    for i in salary:
        print(i.text)

    # ^ - początek linii
    # $ - koniec linii
    # . - dowolny symbol
    # + - nieograniczona liczba elementów
    # '\d' - cyfra
    # '\w' - litera, cyfra, _
    # '\S  - litera


if __name__ == '__main__':
    main()