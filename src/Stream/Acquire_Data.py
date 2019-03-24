import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data

eeg_data, timestamp = inlet.pull_chunk(
        timeout=1, max_samples=int(1 * fs))

# Only keep the channel we're interested in
ch_data = np.array(eeg_data)[:, index_channel]

# Update EEG buffer
Immed_Epoch, filter_state = bf.update_buffer(
        eeg_buffer, ch_data, notch=True,
        filter_state=filter_state)
