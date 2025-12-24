import sys
from pathlib import Path
from urllib.request import urlretrieve
import json

WORKDIR = Path(__file__).parent / 'work'
CLOCKTOWER_SRC = 'https://raw.githubusercontent.com/bra1n/townsquare/develop/src/'


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main(script_name='Trust Issues in Alcatraz'):
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
        if role['id'] == '_meta':
            continue
        role_id = role['id'].replace('_', '').replace('-', '')
        if not (image := MARSEY_MAPPING.get(role_id)):
            missing.append(role_id)
            continue
        role = roles[role_id]
        role['id'] = 'marsey' + role_id
        role['image'] = 'https://rdrama.net/e/' + image
        role_lst.append(role)

    if missing:
        eprint('Missing role images:')
        for it in missing:
            eprint(f"'{it}': '.webp',")
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
    "drunkbinn",
    "byobombs",
    "TracingWoodgrains",
    "BurdensomeCount",
    "idio3",
    "Klenny",
    "hbtz",
    "carpathianflorist",
    "official_techsupport",
    "aqouta",
    "Platy",
    "Skeleton",
    "justcool393",
    "TeachPiece",
]


MARSEY_MAPPING = {
    # townsfolk
    'alchemist': 'marseychimera.webp',
    'amnesiac': 'marseyconfused.webp',
    'artist': 'marseypainter.webp',
    'balloonist': 'marseypinochet.webp',
    'bountyhunter': 'marseybountyhunter.webp',
    'cannibal': 'marseyhannibal.webp',
    'chambermaid': 'marseymaid.webp',
    'clockmaker': 'marseytime.webp',
    'courtier': 'marseychocolatemilk.webp',
    'cultleader': 'marseykeffalsdance.webp',
    'empath': 'marseymeangirls.webp',
    'exorcist': 'marseypope.webp',
    'fool': 'marseyclown2.webp',
    'fortuneteller': 'marseyfortuneteller.webp',
    'gambler': 'marseygambling.webp',
    'gossip': 'marseygossip.webp',
    'king': ' marseyking.webp',
    'lycanthrope': 'marseywerewolf.webp',
    'mathematician': 'marseychartgaussian.webp',
    'mayor': 'marseysoutherner.webp',
    'monk': 'marseymonk.webp',
    'nightwatchman': 'marseybongcop.webp',
    'noble': 'marseycosmopolitan.webp',
    'oracle': 'marseymidsommardani.webp',
    'pacifist': 'marseyinnocent.webp',
    'philosopher': 'marseypipe.webp',
    'preacher': 'marseypastor.webp',
    'sailor': 'marseysailor.webp',
    'innkeeper': 'marseywinemom.webp',
    'juggler': 'marseypearlclutch2.webp',
    'sage': 'marseymonk.webp',
    'seamstress': 'marseyplush.webp',
    'snakecharmer': 'marseyschizosnakeslove.webp',
    # outsider
    'drunk': 'marseydrunk.webp',
    'klutz': 'marseyretard2.webp',
    'moonchild': 'marseymooncricket.webp',
    'politician': 'marseybiden.webp',
    'puzzlemaster': 'marseythinkorino.webp',
    'recluse': 'marseyhorseshoe.webp',
    'saint': 'marseysaint2.webp',
    'sweetheart': 'marseybow.webp',
    'tinker': 'marseythebuilder.webp',
    # minion
    'assassin': 'marseyninja.webp',
    'boomdandy': 'marseyakbar.webp',
    'cerenovus': 'marseycommitted.webp',
    'devilsadvocate': 'marseybaphomet.webp',
    'eviltwin': 'marseynoyou.webp',
    'godfather': 'marseygodfather.webp',
    'legion': 'marseylegion.webp',
    'marionette': 'marseybait.webp',
    'mezepheles': 'marseynotesglow.webp',
    'poisoner': 'marseycyanide.webp',
    'psychopath': 'marseypsycho.webp',
    'scarletwoman': 'marseyfans.webp',
    'spy': 'marseysnekglow.webp',
    'widow': 'marseyspider.webp',
    'witch': 'marseywitch2.webp',
    # demon
    'alhadikhia': 'marseybinladen.webp',
    'fanggu': 'marseyghosthappy.webp',
    'imp': 'marseydevil.webp',
    'pukka': 'marseysnek.webp',
    'shabaloth': 'marseychonker2.webp',
    'vigormortis': 'marseyspookysmile.webp',
    'vortox': 'marseygiygas.webp',
    # traveler
    'barista': 'marseycoffeerecursive.webp',
    'judge': 'marseyjudge.webp',
    # fabled
    'hellslibrarian': 'marseyreading.webp',
    'revolutionary': 'marseyrevolution.webp',
}


if __name__ == '__main__':
    main()
