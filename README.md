# Open Competition 2019
 
 ## Project Description
 
 
 ## How to run...
 ### Requirements
 * A muse headset
 * A bluegiga bled112 bluetooth dongle
 * A MacOS machine (should also work on linux, but it has not been tested)
 * python3
 * To install the required software run `pip install -r requirements.txt`

 ### To run
 Run `python3 src/Stream/muse-lsl.py` from the root of the repository, you should see
 ```
 Found device Muse-XXXX : XX:XX:XX:XX:XX:XX
Connected
Streaming
```
 If you do not try running again.
 
 Then, with the muse on your head, open a new terminal and run 
 ```
 cd src
 python3 main.py
 ```
