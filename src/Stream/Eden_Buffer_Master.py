import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
from Eden_Buffer_Action_Tools import buffer_tools
import Buffer_file as bf



# each trial, add a 0 for false and a 1 for True for the next - doesn't update trial if the Imed_Epoch is bad trial[x] = 0 - add one to dead_trial
if trial < 1:
    Acquire_Stream
    Acquire_Data
    Initialize_Buffer
    buffer_tools.analysis_type()
if trial(==1) <= 5 # change to less than or equal to 5 # 1s in trial
    buffer_tools.update()
else:
    if trial_state[trial[x]-1] == True # if the previous Imed_epoch was free of artifacts and moved over into Current_Epoch - then run the appropriate analysis
        buffer_tools.analysis()

        # acquire data, compute features, visualize raw EEG and the features
        """ 3.1 ACQUIRE DATA """
        # Obtain EEG data from the LSL stream
        eeg_data, timestamp = inlet.pull_chunk(
                timeout=1, max_samples=int(shift_length * fs))

        # Only keep the n_channels we're interested in
        ch_data = np.array(eeg_data)[:, index_channel]

        # Update EEG buffer
        eeg_buffer, filter_state = BCIw.update_buffer(
                        eeg_buffer, ch_data, notch=True,
                        filter_state=filter_state)

                """ 3.2 COMPUTE FEATURES """
        # Get newest samples from the buffer
        data_epoch = bf.get_last_data(eeg_buffer, epoch_length * fs)

        # Compute features
        feat_vector = bf.compute_feature_vector(data_epoch, fs)
        feat_buffer, _ = bf.update_buffer(feat_buffer, np.asarray([feat_vector]))

    buffer_tools.preprocessing()
        if trial_state == True:
            buffer_tools.update()

    if update_current == True

    artifact = False
