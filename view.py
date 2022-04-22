import matplotlib.pyplot as plt
import pandas as pd


with open('pokepalettes.csv', 'r') as f:
    lines = f.readlines()


fig, axs = plt.subplots(151)
fig.suptitle('')

for line in lines:
    res = line.split(',')
    num, pokemon, palette_info = res[0], res[1], res[2:]
