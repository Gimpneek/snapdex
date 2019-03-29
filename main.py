# -*- coding: utf-8 -*-
"""
Main entry point to the bot.

Before initiating the bot the full list of Pokemon is read from the
pokemon.csv file and this is the passed to SnapdexClient instance

The bot is then run using the DISCORD_KEY environment variable
"""
import os
import logging
import csv
from snapdex.snapdexClient import SnapdexClient
from snapdex.pokemonListItem import PokemonListItem

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

all_pokemon = []

with open('pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    for pokemon in list(reader)[1:]:
        alias_list = [] if pokemon[9] == '' else pokemon[9].split('|')
        all_pokemon.append(
            PokemonListItem(
                name=pokemon[1],
                alias_list=alias_list,
                number=pokemon[0],
                types=pokemon[2].split('|'),
                dex_entries=pokemon[8].split('|'),
                sprite=pokemon[7],
                legendary=pokemon[4],
                mythic=pokemon[5],
                regional=pokemon[10])
        )

client = SnapdexClient(pokemon_list=all_pokemon)
client.run(os.environ.get('DISCORD_KEY'))
