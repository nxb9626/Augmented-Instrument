import rtmidi
import time

class midiController:

	def __init__(self):
		
		self.midiout = rtmidi.MidiOut()
		available_ports = self.midiout.get_ports()
		if available_ports:
			self.midiout.open_port(0)
		else:
			print "shit didn't work"
			self.midiout.open_virtual_port("")
	def start_note(self, x):
		note_on = [0x90, x, 112]  # channel 1, middle C, velocity 112
		self.midiout.send_message(note_on)

	def end_note(self, x):
		note_off = [0x80, x, 0]
		self.midiout.send_message(note_off)

