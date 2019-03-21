from muselsl import stream
from pylsl import StreamInlet, resolve_stream


class MuseManager:
    """This class is the singleton controller class that handles the retrieval of the Muse streaming data."""
    
    def __init__(self):
        self.muse_connected = False
        self.__muse = None

    def start_streaming(self):
        '''
        Connects to the muselsl
        '''
        muses = stream.list_muses()

        if(len(muses) < 1):
            print("No Muses found.\n")
        else:
            self.__muse = muses[0]
            self.muse_connected = True
            stream.stream(muses[0]['address'])

        print("Stream has ended\n.")
        
        
    
    def lsl_stream():
        # first resolve an EEG stream on the lab network
        print("looking for an EEG stream...")
        streams = resolve_stream('type', 'EEG')

        # create a new inlet to read from the stream
        inlet = StreamInlet(streams[0])

        while True:
            # get a new sample (you can also omit the timestamp part if you're not
            # interested in it)
            sample, timestamp = inlet.pull_sample()
            print(timestamp, sample)

    def stop_streaming(self):
        raise NotImplementedError
        

    
