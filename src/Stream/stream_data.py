#!/usr/bin/env python                                                                                
import numpy as np
from scipy.signal import butter, lfilter, lfilter_zi, firwin
from time import sleep
from pylsl import StreamInlet, resolve_byprop
from threading import Thread

BUFFER = 12


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
    samples, timestamps = inlet.pull_chunk(timeout=1.0, max_samples=12)
    if timestamps:
        print(samples)
