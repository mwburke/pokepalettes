from PIL import Image
from collections import defaultdict


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def get_palette(img):

    palette_count = defaultdict(int)

    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        pixels = list(img.convert('RGBA').getdata())

        for r, g, b, a in pixels: # just ignore the alpha channel
            if (r + g + b) > 0:
                palette_count[rgb2hex(r, g, b)] += 1

    hex_colors = []
    counts = []
    total_count = 0  # Unused right now due to normalization floating point issues
    for color, count in palette_count.items():
        hex_colors.append(color)
        counts.append(count)
        total_count += count

    counts, hex_colors = zip(*sorted(zip(counts, hex_colors), reverse=True))

    palette_str = ''
    for count, color in zip(counts, hex_colors):
        palette_str += ',{},{}'.format(color, count)

    return palette_str


img_file = 'img/{:03d}_{}.png'


with open('pokemon.csv', 'r') as f:
    lines = f.readlines()



with open('pokepalettes.csv', 'w') as f:

    f.write('number','')

    for i, line in enumerate(lines):
        pokemon = line.rstrip()

        img = Image.open(img_file.format(i + 1, pokemon))

        palette_str = get_palette(img)

        f.write('{:03d},{},{}\n'.format(i + 1, pokemon, palette_str))
