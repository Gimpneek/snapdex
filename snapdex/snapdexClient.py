# -*- coding: utf-8 -*-
""" SnapdexClient Class """
from discord import Client, Embed
import logging
from pokedex.pokedex import Pokedex
from asyncio import TimeoutError
from snapdex.pokedexEntry import PokedexEntry


class SnapdexClient(Client):
    """
    Snapdex, a Discord bot that allows user to collect AR pictures into a
    pokedex
    """

    def __init__(self, pokemon_list, *args, **kwargs):
        super(SnapdexClient, self).__init__(*args, **kwargs)
        self.pokemon_list = pokemon_list
        self.pokedexes = {}
        self.pokemon_images = {}
        self.pokedex = Pokedex()

    async def on_ready(self):
        """
        Handle the bot becoming ready after it's logged in
        """
        logging.info('Logged in as {0}'.format(self.user))

    async def on_message(self, message):
        """
        Handle a message being posted into the chat.

        If the message contains an image then the bot will add the image to the
        list of Pokemon images it stores

        If it's not clear which Pokemon was uploaded (either the user doesn't
        say which Pokemon it is, they indicate multiple Pokemon or the bot
        can't get a clear understanding then the user will be asked to reply
        with which Pokemon it is)

        This method also covers the $snapdex show [POKEMON NAME] command which
        allows the user to show the AR pics they have stored under that
        Pokemon

        :param message: Message posted to Discord channel bot is active in
        :type message: discord.Message
        """
        logging.info(
            'Got message: {0.content} from {0.author}'.format(message))
        if message.author == self.user:
            return
        images = self.get_images(message)
        if images:
            found_pokemon = self.get_pokemon_names(message)
            if not found_pokemon:
                await message.channel.send('Who\'s that Pokemon?')
                await self.handle_pokemon_name_options(message, images[0])
            if len(found_pokemon) > 1:
                options = '{0} or {1}'.format(
                    ', '.join(found_pokemon[:-1]), found_pokemon[-1])
                await message.channel.send(
                    'Which Pokemon is it? {0}?'.format(options))
                await self.handle_pokemon_name_options(message, images[0])
                return
            pokemon_details = \
            self.pokedex.get_pokemon_by_name(found_pokemon[0])
            self.pokemon_images[message.id] = PokedexEntry(
                pokemon_name=found_pokemon[0],
                image=images[0],
                original_message=message,
                details=pokemon_details[0]
            )
            await message.channel.send(
                'That\'s a sick pic of {0}'.format(found_pokemon[0]))

        if '$snapdex show' in message.content:
            found_pokemon = self.get_pokemon_names(message)
            for pokemon in found_pokemon:
                for entry in self.pokedexes.get(message.author, []):
                    if entry.pokemon_name == pokemon:
                        dex_entry = Embed(
                            description=entry.original_message.content,
                            type="rich",
                            title="{0} by {1}".format(pokemon, entry.author),
                            color=0xff2600
                        )
                        dex_entry.set_thumbnail(url=entry.image.url)
                        dex_entry.set_author(
                            name=entry.author,
                            icon_url=entry.author.avatar_url
                        )
                        dex_entry.add_field(
                            name="Name",
                            value=pokemon,
                            inline=True)
                        dex_entry.add_field(
                            name="Pokedex Number",
                            value=entry.details.get('number', ''),
                            inline=True)
                        dex_entry.add_field(
                            name="Types",
                            value="/".join(entry.details.get('types', [])),
                            inline=True)
                        dex_entry.add_field(
                            name="Date Taken",
                            value=entry.original_message.created_at,
                            inline=True)
                        dex_entry.set_footer(
                            text=entry.details.get('description', ''),
                            icon_url=entry.details.get('sprite', '')
                        )
                        await message.channel.send(embed=dex_entry)

    async def on_reaction_add(self, reaction, user):
        """
        Handle an AR pic being reacted to.

        In order for the user to add the AR pic to their Pokedex they need to
        use the :camera_with_flash: emoji

        :param reaction: A discord reaction object, this contains details on
            the emoji used as well as the discord.Message object that the
            reaction was for
        :param user: A discord user object, this is the user that made the
            reaction
        :type reaction: discord.Reaction
        :type user: discord.User
        """
        logging.info('{0} added {1.emoji}'.format(user, reaction))
        if str(reaction.emoji) == '📸':
            message = reaction.message
            images = self.get_images(message)
            if not images:
                await message.channel.send(
                    'You can only add images to your dex')
                return
            if not self.pokedexes.get(user, False):
                self.pokedexes[user] = []
            self.pokedexes[user].append(self.pokemon_images.get(message.id))
            await message.channel.send('Added pic to your dex')

    @staticmethod
    def get_images(message):
        """
        Extract the images in the posted message

        :param message: The message posted to discord
        :type message: discord.Message
        :return: A list of images attached to the message
        :rtype: discord.Attachment[]
        """
        images = []
        for attachment in message.attachments:
            filename = attachment.filename.lower()
            if filename.endswith('.jpg') or filename.endswith('.png'):
                images.append(attachment)
        return images

    def get_pokemon_names(self, message):
        """
        Extract the Pokemon referenced in the posted message

        :param message: The message posted to discord that accompanied the
            AR pic
        :type message: discord.Message
        :return: A list of Pokemon names extracted from the message content
        :rtype: basestring[]
        """
        content = message.content.lower()
        found_pokemon = \
            [word.title() for word in self.pokemon_list if word in content]
        return found_pokemon

    async def handle_pokemon_name_options(self, message, image):
        """
        Handle asking the user to clarify which Pokemon was in the AR pic
        posted.

        This takes advantage of the discord.Client.wait_for method which
        polls the channel for a reply

        :param message: The message for the AR pic
        :param image: The AR pic
        :type message: discord.Message
        :type image: discord.Attachment
        """

        def handle_reply(reply_message):
            """
            Check function called to handle potential reply to the question
            about which Pokemon the user meant in their original post

            :param reply_message: The user's reply
            :type reply_message: discord.Message
            :return: Returns True if the user replies with a Pokemon
            :rtype: bool
            """
            if reply_message.author == message.author:
                reply_pokemon = self.get_pokemon_names(reply_message)
                if len(reply_pokemon) == 1:
                    return True

        try:
            reply = await self.wait_for('message',
                                        timeout=60.0,
                                        check=handle_reply)
        except TimeoutError:
            await message.channel.send('Sorry, you took too long to respond')
        else:
            found_pokemon = self.get_pokemon_names(reply)
            self.pokemon_images[message.id] = PokedexEntry(
                found_pokemon[0], image.url, message.author)
            await message.channel.send(
                'Cool, {0} pic'.format(found_pokemon[0]))
