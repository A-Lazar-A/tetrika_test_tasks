import requests
from bs4 import BeautifulSoup


def task3():
    alphabet = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0,
                'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0,
                'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}
    start_url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%' \
                'B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    main_url = 'https://ru.wikipedia.org/'
    response = requests.get(start_url)

    while True:
        if response.status_code != 200:
            print('Status code isn\'t 200')
            return

        html = BeautifulSoup(response.content, 'lxml')
        url = html.select('#mw-pages')[0].find('a', string='Следующая страница')['href']
        divs_letters = html.select('#mw-pages > div > div')[0]

        for div_letter in divs_letters:
            key = div_letter.find('h3').text.lower()
            # на русской википедии есть животные с английскими названиями
            if key in 'abcdefghijklmnopqrstuvwxyz':
                return alphabet
            animals = div_letter.find('ul').find_all('li')
            alphabet[key] += len(animals)

        response = requests.get(main_url + url)


def main():
    for k, v in task3().items():
        print(f"{k.upper()}: {v}")


if __name__ == '__main__':
    main()
