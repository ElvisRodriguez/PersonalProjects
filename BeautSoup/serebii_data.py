from bs4 import BeautifulSoup
import requests

class SerebiiScraper(object):
    def __init__(self):
        self.names = []

    def _parse_dex_number(self, num):
        if num < 10:
            link = 'https://serebii.net/pokedex-gs/00{n}.shtml'.format(n=num)
            return link
        if num < 100 and num >= 10:
            link = 'https://serebii.net/pokedex-gs/0{n}.shtml'.format(n=num)
            return link
        if num >= 100:
            link = 'https://serebii.net/pokedex-gs/{n}.shtml'.format(n=num)
            return link

    def get_names(self):
        for i in range(1, 252):
            link = self._parse_dex_number(i)
            result = requests.get(link)
            if result.status_code == 200:
                src = result.content
                soup = BeautifulSoup(src, features='html.parser')
                p_tag = soup.find('p')
                table_tag = p_tag.find('table')
                td_tags = table_tag.find_all('td')
                self.names.append(td_tags[13].text)

    def write_names(self):
        with open('gsc_names.txt', 'w') as file:
            for name in self.names:
                file.write(name + '\n')
            file.close()

if __name__ == '__main__':
    ss_obj = SerebiiScraper()
    ss_obj.get_names()
    ss_obj.write_names()
