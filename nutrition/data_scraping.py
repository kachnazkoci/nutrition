import bs4 as bs
import requests
import re


def search_mfp(search_term):
    resp = requests.get('https://www.myfitnesspal.com/food/search?page=1&search=' + search_term)
    soup = bs.BeautifulSoup(resp.text, 'lxml')

    food_item = soup.find('a', href=re.compile('^/food/calories/'))['href']

    resp = requests.get('https://www.myfitnesspal.com' + food_item)
    soup = bs.BeautifulSoup(resp.text, 'lxml')

    nutrition = soup.find('div', 'NutritionalInfoContainer-3XIjH')

    # print('https://www.myfitnesspal.com'+food_item)

    nutritions = [x.getText(separator=u' ') for x in nutrition.find_all('div')]

    base1 = nutritions[0].split('   g ')

    del nutritions[0]

    nutritions = base1 + nutritions

    del nutritions[18]

    nutritions = [x[:-4] if x.endswith('   g') else x for x in nutritions]
    nutritions = [x[:-5] if x.endswith('   mg') else x for x in nutritions]
    nutritions = [x[:-4] if x.endswith('   %') else x for x in nutritions]

    nutritions = ['Calories ' + soup.find('h1').getText()] + nutritions

    return dict(x.rsplit(' ', 1) for x in nutritions)
