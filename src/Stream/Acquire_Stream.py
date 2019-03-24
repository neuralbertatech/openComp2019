import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data

# Search for active LSL stream
print('Looking for an EEG stream...')
streams = resolve_byprop('type', 'EEG', timeout=2)
if len(streams) == 0:
    raise RuntimeError('Can\'t find EEG stream.')

# Set active EEG stream to inlet and apply time correction
print("Start acquiring data")
inlet = StreamInlet(streams[0], max_chunklen=12)
eeg_time_correction = inlet.time_correction()

# Get the stream info, description, sampling frequency, number of channels
info = inlet.info()
description = info.desc()
fs = int(info.nominal_srate())
n_channels = info.channel_count()

# Get names of all channels
ch = description.child('channels').first_child()
ch_names = [ch.child_value('label')]
for i in range(1, n_channels):
    ch = ch.next_sibling()
    ch_names.append(ch.child_value('label'))
