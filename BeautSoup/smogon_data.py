from bs4 import BeautifulSoup
import requests

def import_data():
    names = []
    with open('gsc_names.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            names.append(line.replace('\n', ''))
    return names

def format_url(name):
    return 'https://www.smogon.com/dex/gs/pokemon/{name}/'.format(name=name)

def find_strategies(name):
    link = format_url(name)
    result = requests.get(link)
    if result.status_code == 200:
        src = result.content
        soup = BeautifulSoup(src, features='html.parser')
        span_tag = soup.find('span', {'data-reactid':'.0.1.1.3.6.0.0'})
        if span_tag is None:
            div_tag = soup.find('div', {'data-reactid':'.0.1.1.3.6.0.2'})
            p_tags = div_tag.find_all('p')
            with open('gsc_strats.txt', 'a') as file:
                file.write(name + ':\n')
                for p_tag in p_tags:
                    file.write(p_tag.text + '\n\n')
                file.close()
        else:
            with open('gsc_strats.txt', 'a') as file:
                file.write(name + ' has no strategies\n')
                file.close()

def find_all_strategies(names):
    for name in names:
        find_strategies(name)

if __name__ == '__main__':
    data = import_data()
    # find_strategies('abra')
    # find_all_strategies(data)
