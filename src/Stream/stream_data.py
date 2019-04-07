#!/usr/bin/env python                                                                                
import numpy as np
from scipy.signal import butter, lfilter, lfilter_zi, firwin
from time import sleep
from pylsl import StreamInlet, resolve_byprop
from threading import Thread
import mne
import math
from threading import Thread

# Enough for 1 sec at 256 Hz
BUFFER = 256


print("looking for an EEG stream...")
streams = resolve_byprop('type', 'EEG', timeout=2)

if len(streams) == 0:
    raise(RuntimeError("Cant find EEG stream"))
print("Start aquiring data")

stream = streams[0]

inlet = StreamInlet(stream, max_chunklen=BUFFER)


def alpha(data):
    #data.filter(8, 12, n_jobs=1, l_trans_bandwidth=1, h_trans_bandwidth=1, fir_design='firwin')
    #data.apply_hilbert(n_jobs=1, envelope=False)
    #epochs = mne.Epochs(data, events, 1, -1.0, 3.0, baseline=None, reject=dict(grad=4000e-13, eog=350e-6))
    return np.average([math.sqrt(part.real**2 + part.imag**2) for part in data])


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

#times = []
#count = 0
#chunks = 3
#ave_len = 10
#ave = [0.0, 0.0]
#buf = CircularBuffer(chunks) 

class Stream (Thread):
    def __init__(self):
        Thread.__init__(self)
        # Enough for 1 sec at 256 Hz                                                                               
        self.BUFFER = 256
        print("looking for an EEG stream...")
        self.streams = resolve_byprop('type', 'EEG', timeout=2)
        
        if len(self.streams) == 0:
            raise(RuntimeError("Cant find EEG stream"))
        print("Start aquiring data")

        self.stream = self.streams[0]

        self.inlet = StreamInlet(self.stream, max_chunklen=BUFFER)
        self.times = []
        self.count = 0
        self.chunks = 3
        self.ave_len = 10
        self.ave = [0.0, 0.0]
        self.buf = CircularBuffer(self.chunks)
        self.state = 'noise'
        self._stop_loop = False


    def stop(self):
        self._stop_loop = True


    def run(self):

        while True:
            # Sample is a 2d array of [ [channel_i]*5 ] * BUFFER
            samples, timestamps = self.inlet.pull_chunk(timeout=2.0, max_samples=self.BUFFER)
            if timestamps:
                data = np.vstack(samples)
                data = np.transpose(data)
                print(np.shape(data))
                self.buf.write(data)

            # Check so that the buffer is filled before any filtering
            if self.count >= self.chunks:
                channels = list([0])
                lower_freq = 8
                higher_freq = 12
                filtered_data = mne.filter.filter_data(self.buf.window, 256, lower_freq, higher_freq, filter_length=256*self.chunks-1, fir_design='firwin')
            #for channel in filtered_data:
            #    print(alpha(channel))
                if(self.count < self.chunks+self.ave_len):
                    self.ave[0] += alpha(filtered_data[1]) * (1./self.ave_len)
                    self.ave[1] += alpha(filtered_data[2]) * (1./self.ave_len)
                
                elif(alpha(filtered_data[2]) > self.ave[1]*0.90):
                    if(alpha(filtered_data[1]) > self.ave[0]*1.05):
                        #print('Noise')
                        self.state = 'noise'
                    else:
                        self.state = 'high_alpha'
                        
                else:
                    self.state = 'low_alpha'
                
            self.count += 1
            if self._stop_loop:
                break


if __name__ == '__main__':
    t = Stream()
    t.start()
