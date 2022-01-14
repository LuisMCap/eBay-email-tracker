from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


def get_ebay_url(prompt):
    ebay_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2510209.m570.l1312&_nkw=%s&_sacat=0' % prompt
    return ebay_url


def get_listings(ebay_url):
    r = requests.get(ebay_url).text
    soup = BeautifulSoup(r, features="lxml")

    data = soup.find('ul', {'class': 'srp-results srp-list clearfix'})

    listings = data.find_all('li')

    return listings


def iterate_listings(listings):
    names, prices, links = [], [], []

    for listing in listings:
        if listing.find('h3', {'class': 's-item__title'}) == None:
            continue

        for name in listing.find('h3', {'class': 's-item__title'}):
            if name.text == 'New Listing':
                continue
            names.append(name.text)

        for link in listing.find_all('a', {'class': 's-item__link'}):
            links.append(link['href'])

        temp_price = ''
        for price in listing.find('span', {'class', 's-item__price'}):
            temp_price += price.text
        prices.append(temp_price)

    return names, prices, links


def loop_to_clean_prices(price):
    if 'to' in price:
        price = price.split(' ')[0].replace('$', '')
        try:
            return float(price)
        except ValueError:
            return np.NaN

    else:
        try:
            return float(price.replace('$', ''))
        except ValueError:
            return np.NaN


def clean_prices(prices):
    prices = [loop_to_clean_prices(price) for price in prices]
    return prices


def column_previous_prices(prices):
    previous_prices = ['new entry' for i in range(len(prices))]

    return previous_prices


def column_status(prices):
    status = ['new' for i in range(len(prices))]

    return status


def create_item_data(status, names, prices, previous_prices, links):
    item_data = list(zip(status, names, prices, previous_prices, links))

    return item_data


def make_df(item_data):
    df = pd.DataFrame(item_data, columns=['status', 'name', 'price', 'previous_price', 'link'])

    return df


def get_data_in_df_format(prompt):

    ebay_url = get_ebay_url(prompt)
    listings = get_listings(ebay_url)
    names, prices, links = iterate_listings(listings)

    prices = clean_prices(prices)
    previous_prices = column_previous_prices(prices)
    status = column_status(prices)

    item_data = create_item_data(status, names, prices, previous_prices, links)

    df = make_df(item_data)

    return df
