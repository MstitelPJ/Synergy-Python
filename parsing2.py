from bs4 import BeautifulSoup
import urllib.request


def write_file(url):
    # создаем сессию и отправляем get запрос
    req = urllib.request.urlopen(url)
    html = req.read()
    # запишем html в файл
    with open("index.html", "w", encoding='utf-16') as file:
        file.write(str(html))


write_file('https://www.vedomosti.ru/?utm_source=vedomosti.ru%2Fpartner&utm_medium=main&utm_campaign=desktop_main')

req = urllib.request.urlopen('https://www.vedomosti.ru')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('div', class_='grid-cell__body')
results = []
# print(news)
for item in news:
    title = ''

    if item.find("span", class_="card-article__title") != None:
        title = item.find("span", class_="card-article__title").get_text()
        subtitle = item.find("p", class_="card-article__subtitle")
        if subtitle == None:
            print("Статья:\n" + title + "\n")
        else:
            subtitle = subtitle.get_text()
            print("Статья:\n" + title + "\n       " + subtitle)

        results.append({
            'title': title,
            'subtitle': subtitle,
        })
    elif item.find('div', class_='card-interview__content') != None:
        title = item.find('div', class_='card-interview__content').get_text()
        print("Статья:\n" + title + "\n")
        results.append({
            'title': title,
            'subtitle': None,
        })
    elif item.find('a', class_='card-infoblock__link') != None:
        title = item.find('a', class_='card-infoblock__link').get_text()
        print("Статья:" + title + "\n")
        results.append({
            'title': title,
            'subtitle': subtitle,
        })

f = open('pars.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["subtitle"]}\n\n**********************\n')
    i += 1
f.close()