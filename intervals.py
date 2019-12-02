"""
functions for paying different intervals
m = minor
M = Major
p = perfect
"""
import midiController
m = midiController.midiController()

def play_m2(i):
    x = i+1
    m.start_note(x)
    return x

def play_M2(i):
    x = i+2
    m.start_note(x)
    return x

def play_m3(i):
    x = i+3
    m.start_note(x)
    return x

def play_M3(i):
    x = i+4
    m.start_note(x)
    return x

def play_p4(i):
    x = i+5
    m.start_note(x)
    return x

def play_tritone(i):
    x = i+6
    m.start_note(x)
    return x

def play_p5(i):
    x = i+7
    m.start_note(x)
    return x

def play_m6(i):
    x = i+8
    m.start_note(x)
    return x

def play_M6(i):
    x = i+9
    m.start_note(x)
    return x

def play_m7(i):
    x = i+10
    m.start_note(x)
    return x

def play_M7(i):
    x = i+11
    m.start_note(x)
    return x

def play_octave(i):
    x = i+12
    m.start_note(x)
    return x
#for stopping notes
def stop_m2(i):
    x = i+1
    m.start_note(x)
    return x

def stop_M2(i):
    x = i+2
    m.start_note(x)
    return x
def stop_m3(i):
    x = i+3
    m.start_note(x)
    return x

def stop_M3(i):
    x = i+4
    m.start_note(x)
    return x

def stop_p4(i):
    x = i+5
    m.start_note(x)
    return x

def stop_tritone(i):
    x = i+6
    m.start_note(x)
    return x

def play_p5(i):
    x = i+7
    m.start_note(x)
    return x

def stop_m6(i):
    x = i+8
    m.start_note(x)
    return x

def stop_M6(i):
    x = i+9
    m.start_note(x)
    return x

def stop_m7(i):
    x = i+10
    m.start_note(x)
    return x

def stop_M7(i):
    x = i+11
    m.start_note(x)
    return x

def stop_octave(i):
    x = i+12
    m.start_note(x)
    return x
