butti = """
Discount
disismyaccount
Harpooner
harpooner_
sunshiney
sunshiney
diddy+
goblinbeans
Red_Shill
red_shill
matty [matty]
skwiiid
ATrain Derailed
atrainderailed
Tyrian
tyrianred
baastard (trump's boywife)
anotheruser_
"""

train = """
Harpooner
harpooner_
ATrain Derailed
atrainderailed
Discount
disismyaccount
Techi (Shia)
official_techsupport
sunshiney
sunshiney
McCoxmaul (G127 LVP)
mccoxmaul
matty [matty]
skwiiid
butti tryin 2 make a change 🫤
buttigieg2024
diddy+
goblinbeans
Tyrian
tyrianred
Demy Goonjesh Coomar
demysted
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


votes = (parse(butti) | parse(train)) & everyone
print(f"Voted: {len(votes)}")
print("\n".join(sorted(votes)))
print("\nNot voted:")
print("\n".join(sorted(everyone - votes)))
