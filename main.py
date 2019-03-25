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

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

all_pokemon = []

with open('pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    for raw_pokemon in list(reader)[1:]:
        all_pokemon.append(raw_pokemon[1].lower())

all_pokemon = set(all_pokemon)

client = SnapdexClient(pokemon_list=all_pokemon)
client.run(os.environ.get('DISCORD_KEY'))
