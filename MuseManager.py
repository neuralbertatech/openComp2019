import muselsl as muselsl
from muselsl.muse import Muse
from muselsl.stream import find_muse


class MuseManager:
    """This class is the singleton controller class that handles the retrieval of the Muse streaming data."""
    
    def __init__(self):
        self.stream_alive = False
        self.muse_connected = False
        self.__muse = None

    def start_streaming(self):
        if self.__connect_to_muse():
            pass
            # self.__start_streaming()
        else:
            print("Could not connect to Muse!")
        

    def stop_streaming(self):
        if self.stream_alive and self.muse_connected:
            self.__stop_streaming()
            self.__disconnect()
        else:
            print("The Muse is either not connected or not streaming.\n")

    def __connect_to_muse(self):
        """Connects to the first available Muse."""
        muses = muselsl.list_muses()
        print(muses)
        if not muses:
            return False
        else:
            print("FOUND A MUSE!!!")
            # self.muse_connected = True
            # self.stream_alive = True
            # self.__muse = Muse(muses[0])
            # self.__muse.connect()
            # print("Connected to Muse...\n")
            return True

    
    def __start_streaming(self):
        """Start streaming from the Muse"""
        if self.muse_connected:
            print("Starting stream...\n")
            self.__muse.start()
        else:
            print("Can not start stream if Muse not connected.\n")
            

    def __stop_streaming(self):
        """Stop streaming from the Muse"""
        if self.stream_alive:
            self.__muse.stop()
            self.stream_alive = False
        else:
            print("Muse is not currently streaming.\n") 

    def __disconnect(self):
        """Disconnects from the current Muse."""
        if self.muse_connected:
            self.__muse.disconnect()
            self.muse_connected = False
        else:
            print("Can not disconnect an unconnected Muse.\n")

    
