'''
Title: Pokemon Image Finder
Date Created: 10/14/18
Author: Elvis Rodriguez

Python program that visits Serebii.net and downloads the still model images of
over 800 pokemon using BeautifulSoup. Web scraping made more optimized with
multiprocessing library.
'''
from bs4 import BeautifulSoup
import multiprocessing
import requests

def format_number(number):
    '''
    Formats a number to be used for url indexing.

    Args:
        number: An integer between 1 and 807 inclusive.
    Returns:
        Number casted into a string of the form [0-90-90-9].
    '''
    if number >= 100:
        return str(number)
    if number < 10:
        number = '00{number}'.format(number=number)
    elif number >= 10 and number < 100:
        number = '0{number}'.format(number=number)
    return number

def create_soup_obj(url):
    '''
    Creates a BeautifulSoup Object using a request object drawn from url.

    Args:
        url: A string representing a page on Serebii.net.
    Returns:
        A BeautifulSoup Object using Python 3's default web parser.
    '''
    response = requests.get(url)
    if response.status_code == 200:
        src = response.content
        soup = BeautifulSoup(src, features='html.parser')
        return soup

def create_pokedex_url(dex_no):
    '''
    Creates a url from Serebii.net using dex_no.

    Args:
        dex_no: A number between 1 and 807 inclusive.
    Returns:
        A url formatted with dex_no.
    '''
    dex_no = format_number(dex_no)
    pokedex_url = 'https://serebii.net/pokedex-sm/{dex_no}.shtml'.format(
        dex_no=dex_no
    )
    return pokedex_url

def find_pokemon_name(dex_no):
    '''
    Finds a pokemon's name based off of dex_no using a BeautifulSoup object.

    Args:
        dex_no: A number between 1 and 807 inclusive.
    Returns:
        A string representing a Pokemon's name.
    '''
    url = create_pokedex_url(dex_no)
    soup_obj = create_soup_obj(url)
    td_tags = soup_obj.find_all('td', {'class':'fooinfo'})
    pokemon_name = td_tags[1].text
    return pokemon_name

def create_img_src(dex_no):
    '''
    Creates a Serebii image path using dex_no.

    Args:
        dex_no: A number between 1 and 807 inclusive.
    Returns:
        A string representing an image path.
    '''
    dex_no = format_number(dex_no)
    img_src = '/sunmoon/pokemon/{dex_no}.png'.format(dex_no=dex_no)
    return img_src

def find_image(img_src):
    '''
    Grabs the content of a url using img_src.

    Args:
        img_src: A path to an image on Serebii.
    Returns:
        Binary representation of an image found on the requested url's content.
    '''
    url = 'https://serebii.net/{img_src}'.format(img_src=img_src)
    image = requests.get(url).content
    return image

def obtain_image(dex_no):
    '''
    Finds and downloads a pokemon's image.

    Args:
        dex_no: A number between 1 and 807 inclusive.
    Returns:
        None
    '''
    img_src = create_img_src(dex_no)
    image = find_image(img_src)
    pkmn_name = find_pokemon_name(dex_no)
    print(pkmn_name, 'image downloaded')
    filename = '/assets/pkmn_images/{pkmn_name}.png'.format(pkmn_name=pkmn_name)
    with open(filename, 'wb') as file:
        file.write(image)
        file.close()

if __name__ == '__main__':
    dex_numbers = [x for x in range(1, 808)]
    with multiprocessing.Pool(4) as pool:
        pool.map(obtain_image, dex_numbers)
