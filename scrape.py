import requests
import time


image_url = 'https://img.pokemondb.net/sprites/black-white/normal/{}.png'

with open('pokemon.csv', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    pokemon = line.rstrip()
    img_data = requests.get(image_url.format(pokemon)).content
    with open('img/{:03d}_{}.png'.format(i + 1, pokemon), 'wb') as f:
        f.write(img_data)

    time.sleep(2)
