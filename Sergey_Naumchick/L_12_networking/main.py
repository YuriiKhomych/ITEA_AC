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
def ret_header(name, site):
    response = requests.get(site)
    soup = BS(response.content, 'html.parser')

    titles = soup.find(name)
    return titles.text



if __name__ == '__main__':
    ret_header('title', 'https://stackoverflow.com')
