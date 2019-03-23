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



times = []
while True:
    # Sample is a 2d array of [ [channel_i]*5 ] * BUFFER
    samples, timestamps = inlet.pull_chunk(timeout=2.0, max_samples=BUFFER)
    if timestamps:
        data = np.vstack(samples)
        data = np.transpose(data)
        #print(np.transpose(data))
        #print(np.shape(data))
        print(len(data[0]))
        channels = list([0])
        lower_freq = 5
        higher_freq = 15
        filtered_data = mne.filter.filter_data(data, 256, lower_freq, higher_freq, filter_length=128)
        #filtered_data1 = mne.filter.filter_data(data[1], 256, 5, 15)
        #filtered_data2 = mne.filter.filter_data(data[2], 256, 5, 15)
        #filtered_data3 = mne.filter.filter_data(data[3], 256, 5, 15)
        #filtered_data4 = mne.filter.filter_data(data[4], 256, 5, 15)
        print(filtered_data)
