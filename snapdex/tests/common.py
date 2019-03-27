from snapdex.pokemonListItem import PokemonListItem


POKEMON_NAME = 'Mr. Mime'
ALIAS_ONE = 'Mr Mime'
ALIAS_TWO = 'Creepy Boi'
POKEMON_NUMBER = 122
TYPE_ONE = 'Psychic'
TYPE_TWO = 'Fairy'
SPRITE_URL = 'https://img.pokemondb.net/sprites/red-blue/normal/mr-mime.png'
DEX_ENTRY = """
Mr. Mime is a master of pantomime.
Its gestures and motions convince watchers that somthing unseeable 
actually exists. Once the watchers are convinced, the unseeable thing 
exists as if it were real."""

ITEM_ONE_NAME = 'Mew'
ITEM_ONE_ALIASES = []

ITEM_TWO_NAME = 'Mewtwo'
ITEM_TWO_ALIASES = ['Mew Two']

ITEM_THREE_NAME = 'Haunter'
ITEM_THREE_ALIASES = ['Spooky Boi', 'Spooky Lad']


def get_test_pokemon_list_item():
    """
    Get an example PokemonListItem instance with all values set

    :returns: PokemonListItem instance for Mr. Mime
    :rtype: snapdex.pokemonListItem.PokemonListItem
    """
    return PokemonListItem(
            name=POKEMON_NAME,
            alias_list=[ALIAS_ONE, ALIAS_TWO],
            number=POKEMON_NUMBER,
            types=[TYPE_ONE, TYPE_TWO],
            dex_entries=[DEX_ENTRY],
            sprite=SPRITE_URL,
            legendary=True,
            mythic=True,
            regional=True)


def get_test_pokemon_list():
    """
    Get an example list of PokemonListItems for use with testing

    :returns: list of pokemon
    :rtype: snapdex.pokemonListItem.PokemonListItem[]
    """
    item_one = PokemonListItem(
        name=ITEM_ONE_NAME,
        alias_list=ITEM_ONE_ALIASES)
    item_two = PokemonListItem(
        name=ITEM_TWO_NAME,
        alias_list=ITEM_TWO_ALIASES)
    item_three = PokemonListItem(
        name=ITEM_THREE_NAME,
        alias_list=ITEM_THREE_ALIASES)
    return [item_one, item_two, item_three]
