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
