import sys
from pathlib import Path
from urllib.request import urlretrieve
import json

WORKDIR = Path(__file__).parent / 'work'
CLOCKTOWER_SRC = 'https://raw.githubusercontent.com/bra1n/townsquare/develop/src/'


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main(script_name='Veiled Threats'):
    WORKDIR.mkdir(exist_ok=True)
    roles_json = WORKDIR / 'roles.json'
    if not roles_json.exists():
        eprint('Downloading roles.json')
        urlretrieve(CLOCKTOWER_SRC + 'roles.json', roles_json)

    roles = json.load(roles_json.open())
    roles = {role['id'] : role for role in roles}

    src_file = WORKDIR / (script_name + '.json')
    dst_file = WORKDIR / 'state.json'

    src = json.load(src_file.open())
    role_lst = []
    player_lst = []
    data = {
        'bluffs': [],
        'edition': {
            'id': 'custom',
            'name': script_name + ' (with marseys)'
        },
        'roles': role_lst,
        'players': player_lst,
    }

    missing = []
    for role in src:
        role_id = role['id'].replace('_', '')
        if not (image := MARSEY_MAPPING.get(role_id)):
            missing.append(role_id)
            continue
        role = roles[role_id]
        role['id'] = 'marsey' + role_id
        role['image'] = image
        role_lst.append(role)

    if missing:
        eprint('Missing role images:')
        for it in missing:
            eprint(f"'{it}': 'https://rdrama.net/e/.webp',")
        return

    for name in PLAYERS:
        player_lst.append({
            'name': name,
            'id': '',
            'role': {},
            'reminders': [],
            'isVoteless': False,
            'isDead': False,
            'pronouns': ''
        })

    json.dump(data, dst_file.open('w'))


PLAYERS = [
    'aqouta',
    'Platy',
    'HeyMoon',
    'Redactor0',
    'd20diceman',
    'Substantial',
    'BurdensomeCount',
    'official_techsupport',
    'hbtz',
    'DonGER',
    'justcool393',
    'carpathianflorist',
    'drunkbinn',
]


MARSEY_MAPPING = {
    'noble': 'https://rdrama.net/e/marseycosmopolitan.webp',
    'clockmaker': 'https://rdrama.net/e/marseytime.webp',
    'bountyhunter': 'https://rdrama.net/e/marseybountyhunter.webp',
    'sailor': 'https://rdrama.net/e/marseysailor.webp',
    'balloonist': 'https://rdrama.net/e/marseypinochet.webp',
    'empath': 'https://rdrama.net/e/marseymeangirls.webp',
    'innkeeper': 'https://rdrama.net/e/marseywinemom.webp',
    'exorcist': 'https://rdrama.net/e/marseypope.webp',
    'juggler': 'https://rdrama.net/e/marseypearlclutch2.webp',
    'nightwatchman': 'https://rdrama.net/e/marseybongcop.webp',
    'fool': 'https://rdrama.net/e/marseyclown2.webp',
    'sage': 'https://rdrama.net/e/marseymonk.webp',
    'cannibal': 'https://rdrama.net/e/marseyhannibal.webp',
    'puzzlemaster': 'https://rdrama.net/e/marseythinkorino.webp',
    'tinker': 'https://rdrama.net/e/marseythebuilder.webp',
    'saint': 'https://rdrama.net/e/marseysaint2.webp',
    'politician': 'https://rdrama.net/e/marseybiden.webp',
    'godfather': 'https://rdrama.net/e/marseygodfather.webp',
    'widow': 'https://rdrama.net/e/marseyspider.webp',
    'devilsadvocate': 'https://rdrama.net/e/marseybaphomet.webp',
    'cerenovus': 'https://rdrama.net/e/marseycommitted.webp',
    'fanggu': 'https://rdrama.net/e/marseyghosthappy.webp',
    'chambermaid': 'https://rdrama.net/e/marseymaid.webp',
    'fortuneteller': 'https://rdrama.net/e/marseyfortuneteller.webp',
    'snakecharmer': 'https://rdrama.net/e/marseyschizosnakeslove.webp',
    'monk': 'https://rdrama.net/e/marseymonk.webp',
    'lycanthrope': 'https://rdrama.net/e/marseywerewolf.webp',
    'courtier': 'https://rdrama.net/e/marseychocolatemilk.webp',
    'seamstress': 'https://rdrama.net/e/marseyplush.webp',
    'pacifist': 'https://rdrama.net/e/marseyinnocent.webp',
    'alchemist': 'https://rdrama.net/e/marseychimera.webp',
    'mayor': 'https://rdrama.net/e/marseysoutherner.webp',
    'recluse': 'https://rdrama.net/e/marseyhorseshoe.webp',
    'drunk': 'https://rdrama.net/e/marseydrunk.webp',
    'moonchild': 'https://rdrama.net/e/marseymooncricket.webp',
    'poisoner': 'https://rdrama.net/e/marseycyanide.webp',
    'witch': 'https://rdrama.net/e/marseywitch2.webp',
    'scarletwoman': 'https://rdrama.net/e/marseyfans.webp',
    'pukka': 'https://rdrama.net/e/marseysnek.webp',
    'vigormortis': 'https://rdrama.net/e/marseyspookysmile.webp',
}


if __name__ == '__main__':
    main()
