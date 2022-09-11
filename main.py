import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_URL = 'https://habr.com'
url = base_URL + '/ru/all/'


response = requests.get(base_URL)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__title_h2")
    hubs = [hub.find('span').text for hub in hubs]
    # print(hubs)

for time in articles:
    date_time = article.find_all(class_="tm-article-snippet__datetime-published")
    date_time = [dates.find('time').text for dates in date_time]
    # print((date_time))

for hub in KEYWORDS:
    title = article.find('h2').find('span').text
    href = article.find(class_ = 'tm-article-snippet__title-link').attrs['href']
    result = f' Статьи ---> {title} / {base_URL + href}, {date_time}'
    print(result)

