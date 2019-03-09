# Open Competition 2019

## Things to get first...

 * [Python](https://www.python.org/) (w/ pip)
 * [Git](https://git-scm.com/)
 * Code editor of choice
 * Read through [BCI 101](http://learn.neurotechedu.com/lessons/)
 
 ## Project Description
 
 
 
 ## Modules + Classes
### record
#### class Muse()
def connect(self, interface=None, backend='auto'):
        """Connect to the device, either BLueMuse of pygatt"""
        
def start(self):
        """Start streaming."""
        
def ask_device_info(self):
        """Get status update (hardware version, build number, firmware version, protocol version, return status, if 0 is OK)"""

def ask_control(self):
        """Send a message to Muse to ask for the control status (device name, serial number, MAC address, battery percentage)"""
        
def keep_alive(self):
        """Keep streaming, sending 'k' command"""

def disconnect(self):
        """disconnect."""

def _subscribe_eeg(self):
        """subscribe to eeg stream, asssignment of tags to the streams"""

def _unpack_eeg_channel(self, packet):
        """Decode data packet of one EEG channel.
        Each packet is encoded with a 16bit timestamp followed by 12 time
        samples with a 12 bit resolution.





### muse



### stream
 
 
 
 ## How to run...
