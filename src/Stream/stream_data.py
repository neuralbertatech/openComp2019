#!/usr/bin/env python                                                                                
import numpy as np
from scipy.signal import butter, lfilter, lfilter_zi, firwin
from time import sleep
from pylsl import StreamInlet, resolve_byprop
from threading import Thread
import mne

# Enough for 1 sec at 256 Hz
BUFFER = 256


print("looking for an EEG stream...")
streams = resolve_byprop('type', 'EEG', timeout=2)

if len(streams) == 0:
    raise(RuntimeError("Cant find EEG stream"))
print("Start aquiring data")

stream = streams[0]

inlet = StreamInlet(stream, max_chunklen=BUFFER)

class CircularBuffer:
    def __init__(self, chunks):
        self.window = np.zeros((5, 256*chunks))
        self.chunks = chunks
        self.window_read = self.chunks // 2
        self.window_write = 0
        self.chunk_size = 256

    def read(self):
        #return self.window[:][self.window_read*self.chunk_size:(self.window_read+1)*self.chunk_size]
        return self.window

    def write(self, data):
        self.window[:, self.window_write*self.chunk_size:(self.window_write+1)*self.chunk_size] = data
        self.window_write = (self.window_write + 1) % self.chunks
        self.window_read = (self.window_read + 1) % self.chunks

times = []
count = 0
chunks = 3
buf = CircularBuffer(chunks)

while True:
    # Sample is a 2d array of [ [channel_i]*5 ] * BUFFER
    samples, timestamps = inlet.pull_chunk(timeout=2.0, max_samples=BUFFER)
    if timestamps:
        data = np.vstack(samples)
        data = np.transpose(data)
        print(np.shape(data))
        buf.write(data)

        # Check so that the buffer is filled before any filtering
        if count >= chunks:
            channels = list([0])
            lower_freq = 5
            higher_freq = 15
            filtered_data = mne.filter.filter_data(buf.window, 256, lower_freq, higher_freq, filter_length=256*chunks-1)
            print(filtered_data)

        count += 1
