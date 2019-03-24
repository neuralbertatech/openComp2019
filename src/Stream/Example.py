
    """ 2. SET EXPERIMENTAL PARAMETERS """

    # Length of the EEG data buffer (in seconds)
    # This buffer will hold last n seconds of data and be used for calculations
    buffer_length = 15

    # Length of the epochs used to compute the FFT (in seconds)
    epoch_length = 1

    # Amount of overlap between two consecutive epochs (in seconds)
    overlap_length = 0.8

    # Amount to 'shift' the start of each next consecutive epoch
    shift_length = epoch_length - overlap_length

    # Index of the channel (electrode) to be used
    # 0 = left ear, 1 = left forehead, 2 = right forehead, 3 = right ear
    index_channel = [0, 1, 2, 3]
    # Name of our channel for plotting purposes
    ch_names = [ch_names[i] for i in index_channel]
    n_channels = len(index_channel)

    # Get names of features
    # ex. ['delta - CH1', 'pwr-theta - CH1', 'pwr-alpha - CH1',...]
    feature_names = BCIw.get_feature_names(ch_names)

    """3. INITIALIZE BUFFERS """

    # Initialize raw EEG data buffer (for plotting)
    eeg_buffer = np.zeros((int(fs * 3), n_channels))
    filter_state = None  # for use with the notch filter

    # Compute the number of epochs in "buffer_length" (used for plotting)
))

    # Initialize the feature data buffer (for plotting)
    feat_buffer = np.zeros((n_win_test, len(feature_names)))

    """ 3. GET DATA """

    # The try/except structure allows to quit the while loop by aborting the
    # script with <Ctrl-C>
    print('Press Ctrl-C in the console to break the while loop.')

    try:
        # The following loop does what we see in the diagram of Exercise 1:
        # acquire data, compute features, visualize raw EEG and the features
        while True:

            """ 3.1 ACQUIRE DATA """
            # Obtain EEG data from the LSL stream
            eeg_data, timestamp = inlet.pull_chunk(
                    timeout=1, max_samples=int(shift_length * fs))

            # Only keep the channel we're interested in
            ch_data = np.array(eeg_data)[:, index_channel]

            # Update EEG buffer
            eeg_buffer, filter_state = BCIw.update_buffer(
                    eeg_buffer, ch_data, notch=True,
                    filter_state=filter_state)

            """ 3.2 COMPUTE FEATURES """
            # Get newest samples from the buffer
            data_epoch = BCIw.get_last_data(eeg_buffer,
                                            epoch_length * fs)

            """ 3.3 VISUALIZE THE RAW EEG AND THE FEATURES """
            plotter_eeg.update_plot(eeg_buffer)
            plotter_feat.update_plot(feat_buffer)
            plt.pause(0.00001)

    except KeyboardInterrupt:

        print('Closing!')
