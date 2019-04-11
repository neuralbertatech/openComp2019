# Open Competition 2019
 
 ## Project Description
 
 
 ## How to run...
 ### Requirements
 * A muse headset
 * A bluegiga bled112 bluetooth dongle
 * A MacOS machine (should also work on linux, but it has not been tested)
 * Requires python3

 > install homebrew with

  ` ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" `

 > then install python3 with

  ` brew install python3 `

 > download files using git

  ` git clone https://github.com/neuralbertatech/openComp2019 `


 * To install the required software run `pip install -r requirements.txt`

 > move to project folder 

 ` cd openComp2019 `

 > Configure a virtual environment to contain dependencies

 ` python3 -m venv venv `

 > Activate the environment
 
 ` source venv/bin/activate `


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
