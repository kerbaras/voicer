from voicer.controller import note_on


def run():
    note = input('note -> ')
    while(note != '-1'):
        note_on(int(note))
        note = input('note -> ')