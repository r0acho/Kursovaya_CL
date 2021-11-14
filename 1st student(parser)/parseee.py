import requests, re
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Получение ответов от сервера
def get_html(url):
    r = requests.get(url)
    return r.text

# Получение всех ссылок с сайта
def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    spans = soup.find_all('div', class_='col-md-12 news-item')
    links = []
    for span in spans:
        a = span.find('a').get('href')
        link = 'http://www.volgograd.ru' + a
        links.append(link)

    return links


def cmon(links):
    for url in links:
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        newsTimes = soup.find('div', {'class': 'col-md-9 main-content'}).find('div', {'class': 'date'})
        bigline = soup.find('div', {'id': 'full_text'})
        headline = soup.find('h1').text
        newsLine = bigline.text
        newsLine = re.sub("^\s+|\n|\r|\s+$", '', newsLine)  # 2 текст новости
        newsTime = newsTimes.text.strip()  # 4   дата
        news_ = {
            "headline": headline,
            "text": newsLine,
            "url": url,
            "time": newsTime
        }
        if news.find_one({'headline': headline}) is None:
            if news.find_one({'url': url}) is None:
                if news.find_one({'time': newsTime}) is None:
                    news.insert_one(news_)
                    print('added entry to the database', url)
        else:
            print('entry already exists', url)

f = open('input.txt', 'w')
client = MongoClient()
database = client.prasim
news = database.prasimvolgograd

for i in range(1, 10):
    url = 'https://www.volgograd.ru/news/' + '?PAGEN_1=' + str(i)
    # Список ссылок полученных с сайта
    all_links = get_all_links(get_html(url))
    cmon(all_links)

