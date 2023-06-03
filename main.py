import requests
from dotenv import load_dotenv
import os
import argparse
from urllib.parse import urlparse


def shorten_link(token, link):

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
        }

    data = {
        'long_url': link
        }
    
    response = requests.post(MAINLINK, headers=headers, json=data)
    response.raise_for_status()
    bitlink = response.json()

    return bitlink['id']


def get_link():

    parser = argparse.ArgumentParser(
    description='Описание что делает программа')

    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    return args.link


def count_clicks(token, link):

    headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
    }

    params = {
        'unit': 'day',
        'units': '-1'
    }
    u = urlparse(link)
    response = requests.get(f'{MAINLINK}{u.hostname}{u.path}/clicks/summary', params=params, headers=headers)
    response.raise_for_status()
    click_count = response.json()

    return click_count['total_clicks']


def is_bitlink(token, url):
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
        }
    
    u = urlparse(url)
    response = requests.get(f'{MAINLINK}{u.hostname}{u.path}', headers=headers)
    return response.ok

def main():

    user_link = get_link()

    try:
        
        if is_bitlink(TOKEN, user_link):
            print('Клики:', count_clicks(TOKEN, user_link))

        else:
            print('Битлинк:', shorten_link(TOKEN, user_link))

    except requests.exceptions.HTTPError:
        print("Ошибка! Неверная ссылка")

if __name__ == '__main__':

    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    MAINLINK = os.getenv('MAINLINK')

    main()