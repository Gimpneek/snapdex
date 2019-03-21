import discord
import os
import logging
import csv
from pokedexEntry import PokedexEntry
from asyncio import TimeoutError

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

all_pokemon = []

with open('pokemon.csv', 'r') as f:
  reader = csv.reader(f)
  for raw_pokemon in list(reader)[1:]:
      all_pokemon.append(raw_pokemon[1].lower())

all_pokemon = set(all_pokemon)

pokedexes = {}

pokemon_images = {}


def get_images(message):
    images = []
    for attachment in message.attachments:
        filename = attachment.filename.lower()
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(attachment)
    return images


def get_pokemon_names(message):
    content = message.content.lower()
    found_pokemon = [word.title() for word in all_pokemon if word in content]
    return found_pokemon


async def handle_pokemon_name_options(pokemon, message, image):
    options = '{0} or {1}'.format(', '.join(pokemon[:-1]), pokemon[-1])
    await message.channel.send('Which Pokemon is it? {0}?'.format(options))

    def check(reply_message):
        if reply_message.author == message.author:
            found_pokemon = get_pokemon_names(reply_message)
            if len(found_pokemon) == 1:
                return True

    try:
        reply = await client.wait_for('message',
                                      timeout=60.0,
                                      check=check)
    except TimeoutError:
        await message.channel.send('Sorry, you took too long to respond')
    else:
        found_pokemon = get_pokemon_names(reply)
        pokemon_images[message.id] = PokedexEntry(found_pokemon[0], image.url,
                                                  message.author)
        await message.channel.send('Cool, {0} pic'.format(found_pokemon[0]))


class SnapDexClient(discord.Client):
    async def on_ready(self):
        logging.info('Logged in as {0}'.format(self.user))

    async def on_message(self, message):
        logging.info(
            'Got message: {0.content} from {0.author}'.format(message))
        if message.author == self.user:
            return
        images = get_images(message)
        if images:
            found_pokemon = get_pokemon_names(message)
            if not found_pokemon:
                await message.channel.send('Who\'s that Pokemon?')
            if len(found_pokemon) > 1:
                await handle_pokemon_name_options(
                    found_pokemon, message, images[0])
                return
            pokemon_images[message.id] = PokedexEntry(
                found_pokemon[0], images[0].url, message.author)
            await message.channel.send(
                'That\'s a sick pic of {0}'.format(found_pokemon[0]))
        if '$snapdex show' in message.content:
            found_pokemon = get_pokemon_names(message)
            for pokemon in found_pokemon:
                for entry in pokedexes.get(message.author, []):
                    if entry.pokemon_name == pokemon:
                        await message.channel.send('Heres your {0} pic by {1}: {2}'.format(pokemon, entry.author, entry.image_url))

    async def on_reaction_add(self, reaction, user):
        logging.info('{0} added {1.emoji}'.format(user, reaction))
        if str(reaction.emoji) == '📸':
            message = reaction.message
            images = get_images(message)
            if not images:
                await message.channel.send(
                    'You can only add images to your dex')
                return
            if not pokedexes.get(user, False):
                pokedexes[user] = []
            pokedexes[user].append(pokemon_images.get(message.id))
            await message.channel.send('Added pic to your dex')


client = SnapDexClient()
client.run(os.environ.get('DISCORD_KEY'))
