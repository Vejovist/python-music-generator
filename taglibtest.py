# Import list
import pathlib
import taglib

def meta_change (s = '/pytaglibtest.wav', t = '', u = '', v = '', w = ''):
    SAVELOC = str(pathlib.Path().resolve()) + s

    song = taglib.File(SAVELOC)

    # Change the metadata
    song.tags['DATE'] = [t]
    song.tags['TITLE'] = [u]
    song.tags['ARTIST'] = [v]
    song.tags['GENRE'] = [w]

    print(song.length)

    # Save the metadata
    song.save()
    pass