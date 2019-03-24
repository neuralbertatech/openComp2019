# instead of temporal weighting - use comparison to other bandwidth
# do both and we can pilot
# wavelet - relatively slower

buffer_anal_type = '' # define what you want the analysis type to be '1' = temporally weighted, '2' = inter band comparison, '3' = wavelet

# if trials < 5: add the condition that this is only initialize once
# also have the buffer_tools.analysis_type defined in GameState

class buffer_tools:
    def preprocessing(self): # if an artifcat is detected then skip everything else and wait for appropriate epoch to change state
        bandpass_filt()   # high/low
        if noisy > x
            artifact = True

        return artifact, Current_Cache

    def analysis_type(self):
        if buffer_anal_type == '1': # define elsewhere
            buffer_tools.analysis() = temporal_analysis(Current_Epoch)
        elif buffer_anal_type == '2':
            buffer_tools.analysis() = band_analysis(Current_Epoch)
        elif buffer_anal_type == '3':
            buffer_tools.analysis() = wavelet_analysis(Current_Epoch)
        else:
            buffer_tools.analysis() = temporal_analysis(Current_Epoch)

        return Current_Cache

    def temporal_analysis(Current_Epoch):
        prop_weight = [0.03125,0.0625,0.125,0.25,0.50]
        total_value = 0
        for cache in Last_Cache:
            total value += Last_Cache[cache] * prop_weight[cache]

        winSampleLength, nbCh = eegdata.shape

        # Apply Hamming window
        w = np.hamming(winSampleLength)
        dataWinCentered = eegdata - np.mean(eegdata, axis=0)  # Remove offset
        dataWinCenteredHam = (dataWinCentered.T*w).T

        NFFT = nextpow2(winSampleLength)
        Y = np.fft.fft(dataWinCenteredHam, n=NFFT, axis=0)/winSampleLength
        PSD = 2*np.abs(Y[0:int(NFFT/2), :])
        f = fs/2*np.linspace(0, 1, int(NFFT/2))

        # SPECTRAL FEATURES
        # Alpha 8-12
        ind_alpha, = np.where((f >= 8) & (f <= 12))
        meanAlpha = np.mean(PSD[ind_alpha, :], axis=0)

        feature_vector = np.concatenate((meanAlpha), axis=0)

        feature_vector = np.log10(feature_vector)

        return feature_vector






        return

    def band_analysis(Current_Epoch):

        return

    def wavelet_analysis(Current_Epoch):


    def evaluate()
        if Last_Cache > Current_Cache:
            shoot_speed = slow
        else:
            shot_speed = fast

    def update(epoch):
        Immed_Epoch = # get incoming epoch from muse
        Last_Cache[0] = []
        Last_Cache.append(Current_Cache)
        Current_Epoch = Imed_Epoch

        return *

        

return buffer, shoot_speed
