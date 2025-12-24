n1 = """
diddy+
goblinbeans
Harpooner
harpooner_
matty [matty]
skwiiid
"""

n2 = """
matty [matty]
skwiiid
butti tryin 2 make a change 🫤
buttigieg2024
sunshiney
sunshiney
"""

#############

everyone = frozenset(
    """
    atrainderailed
    buttigieg2024
    demysted
    disismyaccount
    eatmenow
    goblinbeans
    habsburger_
    harpooner_
    mccoxmaul
    official_techsupport
    rabbitcarrot
    red_shill
    skwiiid
    sunshiney
    tyrianred""".split()
)
assert len(everyone) == 15


def parse(s):
    lst = [s2 for s1 in s.split("\n") if (s2 := s1.strip())]
    assert len(lst) % 2 == 0
    return frozenset(lst[1::2])


votes = (parse(n1) | parse(n1)) & everyone
print(f"Voted: {len(votes)}")
print("\n".join(sorted(votes)))
print("\nNot voted:")
print("\n".join(sorted(everyone - votes)))
