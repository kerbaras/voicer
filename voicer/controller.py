import mido
from mido import Message


channel = mido.open_output('voicer', virtual=True)


def note_on(note, velocity=64):
    message = Message('note_on', note=note, velocity=velocity)
    channel.send(message)
