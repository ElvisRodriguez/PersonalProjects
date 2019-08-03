from bs4 import BeautifulSoup
import requests

from serebii_data import SerebiiScraper

MAIN_URL = 'https://serebii.net/'

def create_soup_obj(url):
    response = requests.get(url)
    if response.status_code == 200:
        src = response.content
        soup = BeautifulSoup(src, features='html.parser')
        return soup

def find_pokemon_name(dex_no):
    with open('gsc_names.txt', 'r') as data:
        pkmn_names = data.readlines()
        pkmn_name = pkmn_names[dex_no - 1].replace('\n', '')
    return pkmn_name

def create_pokedex_url(dex_no):
    ss_obj = SerebiiScraper()
    return ss_obj.parse_dex_number(dex_no)

def create_image_url(img_src):
    url = MAIN_URL + img_src
    image_url = requests.get(url).content
    return image_url

def create_target_images(dex_no):
    if dex_no < 10:
        dex_no = '00{n}'.format(n=dex_no)
    elif dex_no >= 10 and dex_no < 100:
        dex_no = '0{n}'.format(n=dex_no)
    target_images = []
    for game in ['gold', 'silver', 'crystal']:
        target_image = '/pokearth/sprites/{game}/{dex_no}.png'.format(
            game=game, dex_no=dex_no
        )
        target_images.append(target_image)
    return target_images

def obtain_images():
    for i in range(1, 252):
        pokedex_url = create_pokedex_url(i)
        soup_obj = create_soup_obj(pokedex_url)
        extensions = ['g', 's', 'c']
        ext_no = 0
        for target_image in create_target_images(i):
            print('Image URL:', target_image)
            image = soup_obj.find('img', {'src':target_image})
            pkmn_name = find_pokemon_name(i)
            filename = 'gsc_sprites/{pkmn_name}-{ext_no}.png'.format(
                pkmn_name=pkmn_name, ext_no=extensions[ext_no]
            )
            print('Filename:', filename)
            with open(filename, 'wb') as file:
                image_url = create_image_url(image['src'])
                file.write(image_url)
                file.close()
            ext_no += 1

if __name__ == '__main__':
    obtain_images()
