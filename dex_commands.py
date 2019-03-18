
all_dex = {'MmmmBeef / 4960 1566 6589': {'Mudkip', 'Wailmer'}, 'gimpneek': {'Zigzagoon', 'Lileep'}}

def get_dex(name):
    if name in all_dex:
        return all_dex[name]
    else:
        return []


def add_to_dex(name, pokemon):
    if name in all_dex:
        all_dex[name].add(pokemon)
        return "Congratulations! " + pokemon + " has been added to " + name + "'s existing dex"
    else:
        return "Congratulations! " + pokemon + " has been added to " + name + "'s brand new dex"


print(add_to_dex('gimpneek', 'Weedle'))
print(get_dex('gimpneek'))

