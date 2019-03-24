""" SET WINDOW + CHANNELS + INITIALIZE BUFFERS"""
# Length of the epochs used to compute the FFT (in seconds)
epoch_length = 1
shift_length = 1
overlap_length = 0
n_channels = 4

# Index of the channel (electrode) to be used
# 0 = left ear, 1 = left forehead, 2 = right forehead, 3 = right ear
index_channel = [0, 1, 2, 3]
ch_names = [ch_names[i] for i in index_channel]
n_channels = len(index_channel)

feature_name = 'Alpha'

Last_Cache = np.zeros((int(fs * 1), n_channels))
Current_Cache = np.zeros((int(fs * 1), n_channels))
Current_Epoch = np.zeros((int(fs * 1), n_channels))
Immed_Epoch = np.zeros((int(fs * 1), n_channels))
Incoming_Epoch =n p.zeros((int(fs * 1), n_channels))
filter_state = None  # for use with the notch filter
