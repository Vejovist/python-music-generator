''' Set-up '''
# Import list
from psonic import *
from random import choice, randint
from time import sleep
from threading import Thread
import pathlib

# Hook up the ports properly
set_server_parameter('127.0.0.1',4557,4559)

''' Classes '''
# Class for tracking the demos
class Dtracker ():
    def __init__ (self):
        # Open file for reading and appending
        demo_tracker = open('demos.txt', 'a+')
        demo_tracker.seek(0) # Bring the cursor to the beginning

        # Read the file and get a value
        demo_num = int(demo_tracker.read()) + 1

        # Write that number back into the file and close it
        demo_tracker.truncate(0) # Clear the file first
        demo_tracker.write(str(demo_num))
        demo_tracker.close()

        # Attribute
        self.num = demo_num
        pass
    pass

# Class for no global variables
class Music ():
    # Initialization
    def __init__ (self, dt):
        # Save Location
        SAVELOC = str(pathlib.Path().resolve()) + '/testsonic' + str(dt.num) + '.wav'

        # Beats Per Minute and Delay Constants
        BPM = 100
        DELAY = 60 / BPM

        ''' How does music theory work again? I forgot. '''
        # List of Scales (See line 59 for RNG)
        scales = [[48, 50, 51, 53, 55, 57, 58], # C Dorian
                  [49, 50, 52, 54, 55, 58, 59], # C# Locrian #6
                  [50, 53, 54, 56, 58, 59, 61], # D Lydian #2 #5
                  [51, 52, 54, 56, 58, 59, 62], # D# Neapolitan Minor
                  [52, 53, 55, 56, 58, 60, 61], # E Super-Locrian bb7
                  [53, 55, 57, 58, 61, 62, 63], # F Mixolydian #5
                  [54, 57, 58, 60, 61, 63, 65], # F# Lydian #2
                  [55, 56, 59, 60, 62, 63, 66], # G Double Harmonic Major
                  [56, 58, 60, 62, 64, 66, 67], # G# Leading Whole-Tone
                  [57, 59, 60, 62, 64, 65, 67], # A Aeolian
                  [58, 59, 62, 63, 65, 66, 68], # A# Phrygian Dominant
                  [59, 61, 62, 65, 66, 68, 70]] # B Lydian b3

        #for n in NOTES: print('%s \t type %g, mode %g' %(n, randint(1, 8), randint(1, 7)))

        # Randomly choose a scale
        main_scale = choice(scales)

        # List of Chords (might be wrong, trying to stick to triads)
        chords = self.set_chords(main_scale)

        # Distinction between bass chords & jazz chords
        bass_chords = chords[:6]

        # Attributes
        self.SAVELOC = SAVELOC
        self.DELAY = DELAY
        self.scales = scales
        self.main_scale = main_scale
        self.chords = chords
        self.bass_chords = bass_chords
        self.tmp = [[], []]
        pass

    # Set the chords
    def set_chords (self, scale):
        chords = [[scale[0], scale[2], scale[4]],            # Major (1 3 5)
                  [scale[0], scale[2] - 1, scale[4]],        # Minor (1 b3 5)
                  [scale[0], scale[2] - 1, scale[4] - 1],    # Diminished (1 b3 b5)
                  [scale[0], scale[2], scale[4] + 1],        # Augmented (1 3 #5)
                  [scale[0], scale[2], scale[6]],            # Major 7th (1 3 7)
                  [scale[0], scale[2], scale[5]],            # Sixth (1 3 6)
                  [scale[0], scale[2], scale[10 % 7] + 13],  # Lydian (1 3 #11)
                  [scale[0], scale[2], scale[12 % 7] + 11],  # Major 7th b13 (1 3 b13)
                  [scale[0], scale[2], scale[6] - 1],        # Dominant 7th (1 3 b7)
                  [scale[0], scale[1], scale[4]],            # Suspended 2nd (1 2 5)
                  [scale[0], scale[3], scale[4]],            # Suspended 4th (1 4 5)
                  [scale[0], scale[3], scale[6] - 1],        # Suspended 4th 7th (1 4 b7)
                  [scale[0], scale[3], scale[8 % 7] + 11],   # Suspended 4th b9 (1 4 b9)
                  [scale[0], scale[2] - 1, scale[5]],        # Minor 6th (1 b3 6)
                  [scale[0], scale[2] - 1, scale[6] - 1],    # Minor 7th (1 b3 b7)
                  [scale[0], scale[4], scale[0] + 12],       # 5th add 1 (1 5 13)
                  [scale[0], scale[2], scale[3]],            # π [3.14...] (1 3 4)
                  [scale[1], scale[5], scale[6] + 1],        # τ [6.28...] (2 6 #7)
                  [scale[0], scale[1], scale[6]],            # e [2.71828...] (1 2 7)
                  [scale[0], scale[2], scale[6]],            # sqrt(3) [1.732...] (1 3 7)
                  [scale[1], scale[2], scale[5]],            # sqrt(5) [2.236...] (2 3 6)
                  [scale[0], scale[5], scale[6] + 1],        # φ [1.618...] (1 6 #7)
                  [scale[0], scale[4] - 2, scale[6]],        # ln i [1.57... i] (1 bb5 7) *
                  [scale[0] - 1, scale[1], scale[6]]]        # i^i [0.207...] (b1 2 7)
        # *Why did anyone ever let me touch instruments ever?

        # Return the list of lists
        return chords

    # Set a temporary scale and chords
    def temp (self):
        self.tmp[0] = choice(self.scales)                   # Scale
        self.tmp[1] = choice(self.set_chords(self.tmp[0]))  # Chords
        pass

''' Naming (and Metadata) '''
def naming (artist = 'judith norwood'):
    # Prefixes (thanks, Google)
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

    # Wait a bit
    sleep(randint(3, 8))

    # Save message
    print('Song saved: %s - %s' %(name, artist))
    pass

''' Generating Music '''
# Bass chords
def bass (m, bars = 6):
    # Instrument
    use_synth(CHIPBASS)

    # Do the number of bars specified
    for i in range(bars):
        # Beats
        mangelwurzel = 0

        # There are 16 beats per bar
        while (mangelwurzel < 16):
            # Increase the beat counter
            mangelwurzel += 1

            # Beat of the bass (starts with a chord)
            bassbeat = choice(m.bass_chords) # Random bass chord
            rnote = choice(m.main_scale)

            # Different bass melody note based on the beat number
            if mangelwurzel == 1: bassbeat.append(bassbeat[0])         # Root
            elif mangelwurzel in [5, 6, 7, 13]: bassbeat.append(rnote) # Random note
            elif mangelwurzel == 9: bassbeat.append(bassbeat[2])       # Highest in chord
            elif mangelwurzel == 15: bassbeat.append(bassbeat[1])      # Third
            else: pass                                                 # Rest

            # Play the chord (and note if it's there)
            play(bassbeat)

            # Wait for the next beat
            print(i + 1, mangelwurzel) # debug
            sleep(m.DELAY)
        pass
    pass

# Main melody
def melody (m, bars = 6):
    # Do the number of bars specified
    for i in range(bars):
        # There are 8 patterns per bar
        for j in range(8):
            # Possible identifiers
            ids = '1234567nNBJC!'

            # Create a pattern
            pattern = '' + choice(ids) + choice(ids) + choice(ids) + choice(ids)

            # Print the pattern
            print(pattern)

            # For each identifier in the pattern
            for id in pattern:
                # Instrument
                use_synth(TRI)

                # Set up a new temporary
                m.temp()

                # Interpret the pattern
                if id in '12345678': play(m.main_scale[int(id) - 1])   # Corresponding note in scale
                elif id == 'n': play(choice(m.main_scale))             # Random note in scale
                elif id == 'N': play(choice(m.tmp[0]))                 # Random note
                elif id == 'B': play(choice(m.bass_chords))            # Random bass chord in scale
                elif id == 'J': play(choice(m.chords))                 # Random chord in scale
                elif id == 'C': play(choice(m.tmp[1]))                 # Random chord
                else: pass                                             # Rest
                
                # Wait
                sleep(m.DELAY / 2)
                pass
            pass
        pass
    pass

# Drums
def drums (m, bars = 6):
    # Do the number of bars specified
    for i in range(bars):
        # There are 8 patterns per bar
        for j in range(8):
            # Possible identifiers
            ids = 'KHHrrrrr'

            # Create a pattern
            pattern = '' + choice(ids) + choice(ids) + choice(ids) + choice(ids)

            # Print the pattern
            print(pattern)

            # For each identifier in the pattern
            for id in pattern:
                # Interpret the pattern
                if id == 'K': choice([sample(ELEC_SOFT_KICK), sample(DRUM_BASS_SOFT)])      # Kick
                elif id == 'H': sample(ELEC_TICK)                                           # Hat
                else: pass                                                                  # Rest
                
                # Wait
                sleep(m.DELAY / 2)
                pass
            pass
        pass
    pass

# Twinglies (not the proper term)
def twinglies (m, bars = 6):
    # Cooldown
    cooldown = 0

    # Do the number of bars specified, 16 beats per bar
    for i in range(bars * 16):
        # Roll a 3-sided die (don't think about it too long)
        di = randint(1, 3)

        # If it's 1 and the cooldown is disabled, and it's on an even beat
        if (di == 1 and cooldown >= 8) and (i + 1) % 2 == 0:
            # Instrument
            use_synth(DARK_AMBIENCE)

            # Play a random twingly
            play(choice(choice(m.bass_chords)) + 24, sustain = 0.1, amp = 0.5, decay = 0.8)

            # Reset the cooldown
            cooldown = 0
            pass

        # Increment the cooldown
        cooldown += 1

        # Wait for the next beat
        sleep(m.DELAY)
        pass
    pass

# Main loop
if __name__ == '__main__':
    # Create a tracker object
    dt = Dtracker()

    # Create a music object
    m = Music(dt)

    # Number of bars
    b = 8

    # Start Recording
    start_recording()

    # Creating threads
    threads = [Thread(target = bass, args = [m, b]), Thread(target = melody, args = [m, b]),
               Thread(target = twinglies, args = [m, b]), Thread(target = drums, args = [m, b])]
    
    # Prevent an abrupt start
    sleep(1)

    # Lead-in (tick, tick, tick, tick)
    for k in range(4):
        sample(ELEC_TICK)
        sleep(m.DELAY)
        pass

    # Play all threads
    for t in threads: t.start()

    # Small wait at the end (prevents song cut-off)
    sleep(1)

    # Wait for input
    input('')

    # Stop and save recording
    stop_recording()
    save_recording(m.SAVELOC)

    # Wait for input again
    input('Waiting for input... ')

    # Ask if alternate artist
    ans = input('Would you like to enter an artist\'s name? (Y/n): ')

    # If so, let the user enter it and name, else name
    if 'y' in ans.lower(): naming(input('Enter an artist name: '))
    else: naming()
    pass