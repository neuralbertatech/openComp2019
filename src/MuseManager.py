import muselsl.stream as stream
from pylsl import StreamInlet, resolve_stream, StreamInfo


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

        if not muses:
            print("No Muses found.\n")
        else:
            # self.__muse = muses[0]
            # self.muse_connected = True
            stream.stream(muses[0]['address'])

        print("Stream has ended\n.")
        

    def stop_streaming(self):
        raise NotImplementedError
        

    
