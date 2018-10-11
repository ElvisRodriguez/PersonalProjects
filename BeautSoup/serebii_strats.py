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

def format_string(string):
    for tag in ['\\n', '<\/p>', '<p>', '<\/h1>', '<p>']:
        string = string.replace(tag, '')

def find_strategies(name):
    link = format_url(name)
    result = requests.get(link)
    if result.status_code == 200:
        print(name)
        src = result.content
        soup = BeautifulSoup(src, features='html.parser')
        script_tag = soup.find('script')
        script_tag = script_tag.next_element.string
        script_string = str(script_tag)
        script_string_list = script_string.split('<p>')
        raw_strategy_text = []
        i = 0
        while i < len(script_string_list):
            if 'overview' in script_string_list[i]:
                raw_strategy_text.extend(script_string_list[i+1:])
                break
        for string in raw_strategy_text:
            format_string(string)
        print(raw_strategy_text)

def find_all_strategies(names):
    for name in names:
        find_strategies(name)

if __name__ == '__main__':
    data = import_data()
    find_all_strategies(['Alakazam'])
