# Import list
from random import choice, randint

# Prefixes (thanks, Google)
def name ():
    prex = ['a', 'ae', 'ambi', 'an', 'ante', 'anti', 'astro', 'auto', 'bin', 'cir',
            'co', 'com', 'con', 'contra', 'contro', 'de', 'dis', 'en', 'epi', 'ex',
            'extra', 'fli', 'gno', 'homeo', 'hyper', 'hyp', 'il', 'im', 'in', 'ir',
            'intra', 'ja', 'ker', 'lat', 'mal', 'meta', 'mid', 'mis', 'mono', 'neo',
            'non', 'ob', 'omni', 'on', 'out', 'para', 'post', 'pre', 'pro', 'quasi',
            'retro', 're', 'semi', 'sub', 'supra', 'sur', 'sym', 'syn', 'tele',
            'tera', 'trans', 'tri', 'ultra', 'un', 'uni', 'up', 'vers', 'wint', 'xe',
            'yet', 'zon']
    
    # Stems
    stem = ['agr' 'arr', 'ced', 'chem', 'chen', 'chron', 'demo', 'derm', 'dict', 'dyn',
            'dys', 'fact', 'fin', 'for', 'fyr', 'geo', 'har', 'heli', 'hood', 'ject',
            'lais', 'leg', 'li', 'lino', 'log', 'magn', 'nor', 'oid', 'phil', 'phob',
            'pod', 'psy', 'pyr', 'qi', 'quin', 'scr', 'se', 'tes', 'thea', 'ther',
            'thra', 'tri', 'var', 'war']
    
    # Suffixes
    sufx = ['ac', 'acy', 'ae', 'ao', 'ary', 'ate', 'dol', 'emu', 'en', 'ence', 'er',
            'ess', 'esque', 'et' 'eux', 'fize', 'ful', 'fy', 'gra', 'i', 'ible', 'ic',
            'imal', 'ine', 'ion', 'ism', 'ist', 'less', 'ly', 'ment', 'nal', 'nym',
            'ola', 'ogy', 'orph', 'ous', 'scope', 'syn', 'th', 'tre', 'ty', 'ude',
            'ure', 'us', 'y', 'yne', 'ysis']

    # Stitching
    name = choice(prex)
    if randint(0, 1) == 0: name += choice(stem)
    else: name += choice('qwertyuiopasdfghjklzxcvbnm')
    if randint(1, 100) % 11 == 0: name += choice('ertyuiopadlxn')
    name += choice(sufx)

    return name

# Produce a few names
for i in range(10): print(name())