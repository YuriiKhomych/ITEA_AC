import requests
from bs4 import BeautifulSoup as BS


def decorate(func):
    def wrapper(name, site):
        with open("answer.txt", "w") as file:
            a = func(site)
            file.write(f'{name} is - {a}')
        print("operation success!")

    return wrapper


@decorate
def ret_header(site):
    response = requests.get(site)
    soup = BS(response.content, 'html.parser')

    titles = soup.find('title')
    return titles.text


def main(site):
    response = requests.get(site)
    soup = BS(response.content, 'html.parser')

    titles = soup.find('title')
    header = soup.find('header')
    print(header)
    print(titles)


if __name__ == '__main__':
    ret_header('title', 'https://stackoverflow.com')
    # main('https://stackoverflow.com/questions?tab=newest&page=1')
